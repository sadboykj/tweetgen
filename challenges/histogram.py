import random
import sys

"""
Histogram() function:
- Takes a source_text argument
- Returns a histogram data structure 
    - Stores each unique word along with 
      the number of times the word appears in the source text.
"""

# Histogram Dictionary

dictOfWords = { i : listOfStr[i] for i in range(0, len(listOfStr) ) }


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