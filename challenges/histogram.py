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
    Pulls all punctuation
    """
    file  = open(text)
    # Converts file to string of lower case words
    words = file.read().lower()
    # Replaces punctuation with nothing
    words = words.translate(str.maketrans('','', string.punctuation))
    # Replaces numbers with nothing
    # words = words.translate(str.maketrans('','', string.digits))

    # Creates list of words from string
    wordlist = [word for word in words.split()]
    """ equivalent to: """
    # wordlist = []
    # file = open(text)
    # for word in file.read().split():
    #     wordlist.append(word)

    file.close()
    return wordlist

# Remove Punctuation Function
# works for text not for files

# def remove_punctuation(text):
#     """
#     Iterates through text
#     Adds everything but punctuation to result
#     """
#     result = ""
#     for char in text:
#         if char not in string.punctuation:
#             print(char)
#             result += char
    
#     return result


# Dictionary Implementation
def histogram(text):
    """
    Histogram() function:
    - Takes a source text argument
    - Stores each unique word
        - along with the number of times the word appears in the source text.
    - Returns a histogram data structure 
    """
    # STRETCH: timing function
    # start = time.time()

    histogram = {}

    # Loads a source text argument
    # Creates list of words
    wordlist = load(text)

    # stores each unique word in histogram
    for word in wordlist:
        
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    # STRETCH: timing function
    # end      = time.time()
    # duration = end - start
    # print("Dictionary Implementation: " + str(duration))

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

def frequency(word, histogram):
    """
    - Takes a word and histogram argument
    - Returns the number of times word appears in text
    """
    # Checks if word is in histogram
    if word in histogram:
        # Returns dictionary value
        return histogram[word]
    else:
        return "Word not found"

def listogram(text):
    """
    Listogram() function:
    - Takes a source text argument
    - Stores each unique word
        - along with the number of times the word appears in the source text.
    - Returns a histogram list data structure 
    """
    # STRETCH: timing function
    # start = time.time()

    listogram = []

    # Loads a source text argument
    # Creates list of words
    wordlist = load(text)

    # stores each unique word in listogram
    for word in range(0, len(wordlist)):
        # print(word)
        # print(wordlist[word])
        if len(listogram) == 0:
            listogram.append([wordlist[word], 1])
        else:
            if wordlist[word] not in listogram:
                listogram.append([wordlist[word], 1])
            else:
                listogram[i][1] += 1

    # STRETCH: timing function
    # end      = time.time()
    # duration = end - start
    # print("List Implementation: " + str(duration))

    # Returns a histogram list data structure
    return listogram


if __name__ == '__main__':

    file = sys.argv[1]
    # hist = histogram(file)
    hist = listogram(file)
    
    # print(frequency("fish", hist))
    print(hist)