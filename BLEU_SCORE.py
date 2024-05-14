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


c = "The quick brown fox jumps over the lazy dog."
r = "A quick brown fox leaped over the lazy dog."

print(make_ngrams(sentence=c, n=1))
