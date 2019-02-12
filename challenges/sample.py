import random, sys, re, string
from histogram import load, histogram

"""
GOAL: To pull words out of the histogram to produce sentences

Stochastic sampling
- taking an element from a given collection at random
- giving each element weight based on its frequency
"""

def sample(text):
    
    # converts text to histogram
    histo = histogram(text)
    # print("histogram: ")
    # print(histogram)

    # returns number of tokens in histogram
    tokens = 0
    for word in histo:
        tokens += histo[word]
    # print("tokens: ")
    # print(tokens)
    
    # cumulative_probability
    cum_prob = 0

    # random number
    ranum = random.uniform(0, 1)
    # print("random number: ")
    # print(ranum)

    # randomly picks one word based on word frequency
    for word in histo:
        cum_prob += (float(histo[word]) / float(tokens))
        # print("cumulative prob: ")
        # print(cum_prob)
        if cum_prob >= ranum:
            return word

def test(text):
# def test(text, iterations):

    histo = dict()

    # if iterations is None:
    #     iterations = 500

    for i in range(0, 50):
        
        word = sample(text)

        # for parsing through keys
        # if word in words.keys()
        if word in histo:
            histo[word] += 1
        else:
            histo[word] = 1

    return histo

def sentence(text):

    histo  = test(text)

    result = ""

    length = 0

    while length < 140:
        for word in histo:
            result += " "
            result += str(word)
            length += len(word)
    
    # takes out beginning space character from line 73
    # capitilizes new first letter
    # adds period to the end
    result = result[1:].capitalize() + "."

    return result

    
    # for _ in range(random.randint(10, 30)):
    #     newSentenceArray.append(word_selection(histogram))
    # return " ".join(newSentenceArray) + "."

if __name__ == '__main__':
    
    file     = sys.argv[1]
    # result   = sample(file)
    # test     = test(file)
    sentence = sentence(file)

    print(sentence)
    