import random
import sys
import timeit
import linecache

"""
Returns random dictionary words
"""

def load(text):
    """
    Load words from a file
    """
    file = open(text, 'r')
    words = file.readlines()
    return words

def random_load(count, text):
    """
    Randomly selects words from a text
    """
    words = []

    for c in range(0, count):
        word = text[random.randint(0, len(text) - 1)]
        words.append(word.rstrip('\n'))

    return words

def line_cache(count):
    """
    Uses Line Cache to pull random sentences fast
    Text Amount must be defined
    """
    text = 235886 # number of words in dictionary
    words = []

    for i in range(0, count):
        r = random.randint(0, text - 1)
        word = linecache.getline("/usr/share/dict/words", r).rstrip('\n')
        words.append(word)

    return words

def compare() :
    """
    Edge Casing
    """
    if len(sys.argv) != 2:
        print("Make sure to add a number at the end of the command")
        print('Example usage: python dictionary_words.py 10')
        sys.exit()

    else: 

        if sys.argv[1] == 'test':

            # Test 1
            setup = 'from dictionary_words import load, random_select;'
            print('Test 1 took: \n')
            print(timeit.timeit(stmt='random_select(10, load("/usr/share/dict/words"))', setup=setup, number=100), end=" ")

            # Test 2
            setup = 'from dictionary_words import lc_select'
            print('Test 2 took: \n')
            print(timeit.timeit(stmt='lc_select(10)', setup=setup, number=100), end=" ")

        if sys.argv[1] == 'vocab':
            """
            Users can input their answers
            Users are shown the answer afterward
            """
        #     # Slow test
        #     print('Getting 10 random words the slow way:')
        #     setup = 'from dictionary_words import load_words, randomly_select;'
        #     print('It took:', end=' ')
        #     print(timeit.timeit(stmt='randomly_select(10, load_words("/usr/share/dict/words"))', setup=setup, number=100), end=" ")
        #
        #     # Fast test
        #     print('Getting 10 random words the fast way:')
        #     setup = 'from dictionary_words import fast_select'
        #     print('It took:', end=' ')
        #     print(timeit.timeit(stmt='fast_select(10)', setup=setup, number=100), end=" ")
        #     print('seconds')
        else:
            count = int(sys.argv[1])
            words = lc_select(count)

            for word in words:
                print(word, end=' ')

            print()

if __name__ == '__main__':
    
