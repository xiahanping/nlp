from collections import Counter
import numpy as np


def tf(word:str, doc:str) -> int:

    words_list = doc.split()
    words_cnt = Counter(words_list)

    return words_cnt[word]

def df(word:str, corpus:list) -> int:
    return sum(1 for doc in corpus if word in doc)

def idf(word:str, corpus:list) -> float:
    return np.log10(len(corpus) / (df(word, corpus) + 1))


