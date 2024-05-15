import numpy as np
from collections import Counter
import re


def make_ngrams(sentence, n: int):
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


def make_ngrams_dataset_counted(references):
    """
        Create counted ngrams set dataset for given reference/s.
    """
    ds = []
    for ref in references:
        for n in range(1, len(ref.split()) + 1):
            ng = set(make_ngrams(sentence=ref, n=n))
            if ng not in ds:
                ds.extend(ng)
    # print(Counter(ds))
    return Counter(ds)


def cleaner(strings):
    for i in range(len(strings)):
        strings[i] = re.sub(r'[^\w\s]', '', strings[i])
    return strings


def precision(candidate, couted_ref_ngrams, n=1):
    """
    Calculate precision for a given candidate and list of references.
    https://www.cl.uni-heidelberg.de/courses/ss15/smt/scribe8.pdf
    """
    count_clip = 0
    candidate_ngram = make_ngrams(sentence=candidate, n=n)
    candidate_ngram_counts = Counter(candidate_ngram)
    for ngram in set(candidate_ngram):
        # print(ngram)
        max_count = min(couted_ref_ngrams[ngram], candidate_ngram_counts[ngram])
        count_clip += min(max_count, candidate_ngram_counts[ngram])  # number of times matching canditate ngrams
    return count_clip / sum(candidate_ngram_counts.values())


c = "The quick brown fox jumps over the lazy dog."
c = cleaner(strings=[c])[0]
r = "A quick brown fox leaped over the lazy dog."
refs = [r]
ref_ngram_ds = make_ngrams_dataset_counted(references=refs)
# print(precision(candidate=c, couted_ref_ngrams=ref_ngram_ds, n=1))

# print(make_ngrams(sentence=c, n=1))
# done make_ngrams
# print(make_ngrams_dataset_counted(references=[c]))
# done make_ngram_dataset_counted
# print(precision(candidate=c, couted_ref_ngrams=ref_ngram_ds, n=1))
# done precision



c = 'A cat sat on the mat'
c = cleaner(strings=[c])[0]
r1 = 'The cat is on the mat.'
r2 = 'There is a cat on the mat.'
refs = [r1, r2]
refs = cleaner(strings=refs)
ref_ngram_ds = make_ngrams_dataset_counted(references=refs)
# print(modified_precision(candidate=c, couted_ref_ngrams=ref_ngram_ds, n=1))
print(precision(candidate=c, couted_ref_ngrams=ref_ngram_ds, n=1))

# print(ref_ngram_ds)
# c = 'the the the the the the the'
# c = cleaner(strings=[c])[0]
# r1 = 'The cat is on the mat.'
# r2 = 'There is a cat on the mat.'
# refs = [r1, r2]
# refs = cleaner(strings=refs)
# ref_ngram_ds = make_ngrams_dataset_counted(references=refs)
# print(modified_precision(candidate=c, couted_ref_ngrams=ref_ngram_ds, n=1))
# print(precision(candidate=c, couted_ref_ngrams=ref_ngram_ds, n=1))



