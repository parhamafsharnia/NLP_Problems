import numpy as np
from collections import Counter


def make_ngrams(sentence, n):
    """
    Create n-grams from a given sentence.
    Inputs:
    n -> int: n-gram size - (max: sentence length, ow [])
    sentence -> str: sentence to get n-grams.
    Output:
    ngrams -> list: list of n-grams
    """
    words = sentence.lower().split()
    ngrams = []
    for i in range(len(words) - n + 1):
        ngrams.append(' '.join(words[i: i + n]))
    return ngrams


def make_ngrams_dataset(references):
    ds = []
    for ref in references:
        for n in range(1, len(ref.split()) + 1):
            ng = make_ngrams(sentence=ref, n=n)
            if ng not in ds:
                ds.extend(ng)
    return ds


c = "The quick brown fox jumps over the lazy dog."
r = "A quick brown fox leaped over the lazy dog."

# print(make_ngrams(sentence=c, n=1))
# done make_ngrams
# print(make_ngrams_dataset(references=[c]))
# done make_ngram_dataset

