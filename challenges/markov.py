#!python3

import random, sys, re, string
from histogram import load, histogram, unique_words

def markov(text):
    histo = histogram(text)
    chain = {}

    for key, value in histo.items():
        print(key, value)

    # dictionary in dictionary

    # see which word comes after start
    # check if word is in next list
    # add (word, +1) to next list as value

    return



if __name__ == '__main__':
    file = sys.argv[1]

    # TEST MARKOV
    markov(file)