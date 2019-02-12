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

    histo = dict()

    for i in range(0, 10000):
        
        word = sample(text)

        # for parsing through keys
        # if word in words.keys()
        if word in histo:
            histo[word] += 1
        else:
            histo[word] = 1

    return histo

def create_sentence(text):
    
    newSentenceArray = []
    for _ in range(random.randint(10, 30)):
        newSentenceArray.append(word_selection(histogram))
    return " ".join(newSentenceArray) + "."

if __name__ == '__main__':
    
    file   = sys.argv[1]
    result = sample(file)
    test   = test(file)

    print(test)
    

# def create_probability_dict(histogram, loop=10000):
#     prob_dict = {}

#     for item in histogram:
#         prob_dict[item[0]] = 0

#     for _ in range(0, loop):
#         prob_dict[word_selection(histogram)] += 1

#     return prob_dict