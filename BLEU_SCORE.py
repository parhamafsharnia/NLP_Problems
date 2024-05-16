from collections import Counter
import re


def make_ngrams(sentence: str, n: int):
    """
    Create n-grams from a given sentence.
    Inputs:
    n -> int: n-gram size - (max: sentence length, ow [])
    sentence -> str: sentence to get n-grams.
    Output:
    ngrams -> list: list of n-grams
    """
    # print(sentence)
    words = sentence.lower().split()
    ngrams = []
    for i in range(len(words) - n + 1):
        ngrams.append(' '.join(words[i: i + n]))
    return ngrams


def make_ngrams_dataset_counted(references: list):
    """
        Create counted ngrams dataset for given reference/s.
        Inputs:
        references -> list: list of refrences.
        Output:
        Counter(ds) -> dict: dictionary of counted n-grams
    """
    ds = []
    for ref in references:
        for n in range(1, len(ref.split()) + 1):
            ng = make_ngrams(sentence=ref, n=n)
            if ng not in ds:
                ds.extend(ng)
    return Counter(ds)


def cleaner(strings: list):
    """
            remove punctuations from given sentence.
            Inputs:
            strings -> list: list of straings.
            Output:
            strings -> list: list of clean straings.
        """
    for i in range(len(strings)):
        strings[i] = re.sub(r'[^\w\s]', '', strings[i]).strip()
    return strings


def precision(candidate, counted_ref_ngrams, n=1):
    """
    Calculate precision for a given candidate and list of references.
    https://thepythoncode.com/article/bleu-score-in-python
    """
    count_clip = 0
    candidate_ngram = make_ngrams(sentence=candidate, n=n)
    candidate_ngram_counts = Counter(candidate_ngram)
    for ng in candidate_ngram:
        matched = min(counted_ref_ngrams[ng], candidate_ngram_counts[ng])  # number of times matching canditate ngrams
        count_clip += matched
    return count_clip / sum(candidate_ngram_counts.values())


def brevity_penalty(candidate_length, reference_length):
    import math
    """
    Calculate the brevity penalty for a given candidate and reference.
    """
    if candidate_length > reference_length:
        return 1
    else:
        return math.exp(1 - reference_length / candidate_length)


def calculate_bleu(candidate, counted_reference, references, n=4):
    import math
    """
    Calculate the BLEU score for a given candidate and list of references.
    """
    # Calculate the modified precision for each n-gram order
    precisions = []
    counter = n
    for i in range(1, n + 1):
        p_n = precision(candidate=candidate, counted_ref_ngrams=counted_reference, n=i)
        if p_n != 0:
            precisions.append(p_n)
        else:
            counter -= 1
    # Calculate the brevity penalty
    print(precisions)
    bp = brevity_penalty(candidate_length=len(candidate.split()),
                         reference_length=min(len(ref.split()) for ref in references))
    # Calculate the BLEU score
    weights = [1 / counter] * counter
    bleu = bp * math.exp(sum(w * math.log(p) for w, p in zip(weights, precisions)))
    return bleu, counter


# unit test
# print(make_ngrams(sentence=c, n=4))
# done make_ngrams
# print(make_ngrams_dataset_counted(references=[c]))
# done make_ngram_dataset_counted
# print(precision(candidate=c, couted_ref_ngrams=ref_ngram_ds, n=1))
# done precision
# print(brevity_penalty(candidate_length=len(r1), reference_length=len(c)))
# done brevity penalty
# print(calculate_bleu(candidate=c, counted_refrence=ref_ngram_ds, references=refs, n=4))
# done calcualte bleu score
# finish

# test1
c = "Thez quick brown fox jumps over the lazy dog."
c = cleaner(strings=[c])[0]
r = "A quick brown fox leaped over the lazy dog."
refs = [r]
refs = cleaner(strings=refs)
ref_ngram_ds = make_ngrams_dataset_counted(references=refs)
bleu_score, ngram = calculate_bleu(candidate=c, counted_reference=ref_ngram_ds, references=refs, n=4)
print(f'BLEU Score: {bleu_score}\n n-grams from {1, ngram}')

# # test2
# c = 'A cat sat on the mat'
# c = cleaner(strings=[c])[0]
# r1 = 'The cat is on the mat.'
# r2 = 'There is a cat on the mat.'
# refs = [r1, r2]
# refs = cleaner(strings=refs)
# ref_ngram_ds = make_ngrams_dataset_counted(references=refs)
# bleu_score, ngram = calculate_bleu(candidate=c, counted_reference=ref_ngram_ds, references=refs, n=4)
# print(f'BLEU Score: {bleu_score}\n n-grams from {1, ngram}')
