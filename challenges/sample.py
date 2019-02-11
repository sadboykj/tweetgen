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
    words = histogram(text)
    # print(words)

    # returns length of histogram
    count = len(words) - 1
    # print(count)
    
    # cumulative_probability
    cum_prob = 0

    # random number
    ranum = random.uniform(0, count)

    # randomly picks one word based on word frequency
    for word in words:
        cum_prob += (float(words[word]) / float(count))
        if cum_prob >= ranum:
            return word


# def sample(histogram):
#     total_sum = 0
#     cumulative_prob = 0.0

#     for item in histogram:
#         total_sum += item[1]

#     random_num = random.uniform(0, 1)
#     for value in histogram:
#         cumulative_prob += float(value[1]) / float(total_sum)
#         if cumulative_prob >= random_num:
#             return value[0]

def test(text):

    words = dict()

    for i in range(0, 10):
        
        word = sample(text)
        print(word)

        # for parsing through keys
        # if word in words.keys()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    print(words)



if __name__ == '__main__':
    
    file   = sys.argv[1]
    result = sample(file)
    test = test(file)

    print(result)
    


# def create_sentence(histogram):
#     newSentenceArray = []
#     for _ in range(random.randint(10, 30)):
#         newSentenceArray.append(word_selection(histogram))
#     return " ".join(newSentenceArray) + "."

# def create_probability_dict(histogram, loop=10000):
#     prob_dict = {}

#     for item in histogram:
#         prob_dict[item[0]] = 0

#     for _ in range(0, loop):
#         prob_dict[word_selection(histogram)] += 1

#     return prob_dict