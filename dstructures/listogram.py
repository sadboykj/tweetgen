#!python3
# pip3 install --user pytest

from __future__ import division, print_function  # Python 2 and 3 compatibility

class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # adds count to total token amount
        self.tokens += count

        """
        iterates through Listogram
        checks if word is in list
        then increases frequency
        
        if it isnt in lists
        it adds a new word type
        then adds the word to the list
        """

        # ATTEMPT #2

        for item in self:
            if item[0] == word:
                item[1] += count
            else:
                self.types += 1
                self.append([word, count])
                print([word,count])
        
        return

        # ATTEMPT #1

        # for list 
        # if word in self:
        #     self[word] += count
        # else:
        #     self.types += 1
        #     self[word] = count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        for item in self:
            # Retrieve word frequency count
            if item[0] == word:
                return item[1]
            else:
                return 0


    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        for item in self:
            # Check if word is in this histogram
            if item[0] == word:
                return True
            else:
                return False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # ATTEMPT #2
        # utilizing enumerate
        for index, item in enumerate(self):
            if item[0] == target:
                return index

        return None

        # ATTEMPT #1
        # Implement linear search to find index of entry with target word
        # index = 0
        # for item in self:
        #     if target == item[0]:
        #         return index
        #     index += 1
        # return None

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()