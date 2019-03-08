#!python3
import random, sys, re, string, time
from dictogram import Dictogram
# from Stochastic import *
# from Modules import *

def load(text):
    """
    Loads file as list of words
    Pulls all punctuation
    """
    file  = open(text)
    # Converts file to string of lower case words
    words = file.read().lower()
    # Replaces punctuation with nothing
    words = words.translate(str.maketrans('','', string.punctuation))

    # Creates list of words from string
    wordlist = [word for word in words.split()]
    """ equivalent to: """
    # wordlist = []
    # file = open(text)
    # for word in file.read().split():
    #     wordlist.append(word)

    file.close()
    return wordlist

def dicto(words):
    # initialize dictionary
    d = {}
    
    # iterate through word arrray
    # add words if not in d
    for word in words:
        if word not in d.keys():
            d[word] = {}
    
    # add counts
    index = 0
    for word in words:
        if len(words) > index + 1:
            next = words[index + 1]
            if next in d[word].keys():
                d[word][next] += 1
            else:
                d[word][next] = 1
            index += 1
    print(d)
    return d

def randWalk(dicto):
    # initialize sentence
    sentence = ""
    length = 0
    # choose random starting word
    start = random.choice(list(dicto))
    histo = dicto[start]

    sentence += start
    length += len(start)

    # sample words
    while(length < 140):
        print("check if loop works")
        # start walk
        for word in histo:
            print(word)
            types = len(histo)
            tokens = sum(histo.values())
            cum_prob = 0
            ranum = random.uniform(0, 1)

            cum_prob += (float(histo[word]) / float(tokens))
            if cum_prob >= ranum:
                sentence += " " + word
                length += len(word)
                print(length)

        # go on to next word
        histo = dicto[word]

        # returns sentence if new word hist empty
        if not histo:
            print("End")
            sentence = sentence[0:].capitalize() + "."
            return sentence

    # capitilizes first word
    # adds period at the end
    sentence = sentence[0:].capitalize() + "."
    return sentence

def main():
    dicto_gram = dicto(load('edgarallenpoe.txt'))
    sentence = randWalk(dicto_gram)
    return sentence

if __name__ == "__main__":
    print(main())