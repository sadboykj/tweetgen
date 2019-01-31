import random
import sys

"""
unique_words() function:
- takes a histogram argument 
- returns the total count of unique words
"""

# def unique_words(Histogram):

def load(text):
    """
    Loads words from dictionary
    """
    # Dictionary pull shortcut
    # wordList = [line.strip() for line in open('/usr/share/dict/words')]

    file  = open(text, 'r')
    loads = file.readlines()
    words = [word.strip() for word in loads]
    # equivalent to:
    # words = []
    # for word in loads:
    #     words.append(word.strip())

    file.close()
    return words

if __name__ == '__main__':
    print()