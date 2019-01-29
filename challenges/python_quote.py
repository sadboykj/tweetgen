import random
import sys

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

def random_python_quote():
    rand_index = random.randint(0, len(quotes) -1)
    return quotes[rand_index]

def reverse_words(*args):
    word_list = []
    c = len(args) - 1
    while c >= 0:
        word_list.append(args[c])
        c-=1
    return " ".join(word_list)

def reverse_sentences():
    sentence_list = []
    c = len(args) - 1
    while c > 0:
        sentence_list.append(args[c])
    return sentence_list

if __name__ == '__main__':
