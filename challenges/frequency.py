import random
import sys

"""
Frequency() function:
- takes a histogram argument 
- returns the number of times that word appears in a text
"""

# def frequency(Histogram):

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