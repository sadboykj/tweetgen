"""Autocomplete Dictionary Input Challenge"""

import sys
import itertools

def load(text):
    """
    Loads words from dictionary
    """
    file  = open(text, 'r')
    words = file.readlines()
    file.close()
    return words

def anagram(word, text):
    """
    Adds anagrams from dictionary from input
    Stops game if no words found
    """
    # initialize autocomplete word list
    # anagrams = ["".join(perm) for perm in itertools.permutations(word)]

    # # iterates through text to find matches
    # for line in text:
    #     if line.startswith(word):
    #         anagrams.append(line)

    # # no anagrams found
    # if len(anagrams) == 0:
    #     print("No words found!")
    #     sys.exit(1)

    return anagrams

def game():
    print("\nWelcome to Anagram\n")

    word = input("Give me a word\n\n")
    # checks emptiness
    if not word:
        print("You must enter a word\n")
        sys.exit(1)

    loads    = load("/usr/share/dict/words")
    anagrams = anagram(str(word), loads)
    found    = print("{} anagrams were found".format(len(anagrams)))
    results  = print(anagrams)
    
    # c = 0
    
    # while c < results:
    #     sentence = "    {}.    {}".format((count + 1), anagrams[count])
    #     print(sentence)
    #     count += 1

if __name__ == '__main__':
    # game()
    anagrams = ["".join(perm) for perm in itertools.permutations("word")]
    print(anagrams[0])
