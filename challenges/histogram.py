import random, sys, re, string, time

def load(text):
    """
    Loads words from dictionary
    """
    # Dictionary pull shortcut
    # wordList = [line.strip() for line in open('/usr/share/dict/words')]

    """ 
    Loads whole file as string
    """
    # loads = file.readlines()
    # words = [word.strip() for word in loads]
    """ equivalent to """
    # words = []
    # for word in loads:
    #     words.append(word.strip())

    """
    Loads file as list of words
    """
    # wordlist = []
    # file = open(text)
    # for word in f.read().split():
    #     wordlist.append(word)
    """ equivalent to: """
    file  = open(text)
    words = [word for word in file.read().split()]

    file.close()
    return words

# Dictionary Implementation
def histogram(text):
    """
    Histogram() function:
    - Takes a source_text argument
    - Stores each unique word
        - along with the number of times the word appears in the source text.
    - Returns a histogram data structure 
    """
    # STRETCH: timing function
    start = time.time()

    histogram = {}

    # Takes a source text argument
    words = load(text)

    # stores each unique word
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    # STRETCH: timing function
    end      = time.time()
    duration = end - start
    print("Dictionary Implementation: " + str(duration))

    # Returns a histogram dictionary data structure
    return histogram

def unique_words(histogram):
    """
    - Takes a histogram argument
    - Returns total count (integer) of unique words
    """

    # Takes a histogram argument
    # Returns total count of unique words
    return len(histogram)

    # for w in wl:
    #     count = 0
    #     print(w)

    # for w in ws:
    #     if(w == wl):
    #         count += 1
    #         print(w, count)
    #         # print(couple)

# dictOfWords = { i : listOfStr[i] for i in range(0, len(listOfStr) ) }


if __name__ == '__main__':

    # print(wordlist)
    # print(wordfrequency(wordlist, text))
    file = sys.argv[1]
    my_dict = histogram(file)
    print(my_dict)