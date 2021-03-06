#!python

from linkedlist import *


class HashTable(object):

    def __init__(self, init_size=8):
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size    = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table."""
        """Running time: O(n^n) double for loop iterates through bucket values"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table."""
        """Running time: O(n^n) double for loop iterates through bucket values"""
        # Modeled after keys function
        all_values = []
        # Loop through all buckets
        for bucket in self.buckets:
            # Collect all values in each bucket
            for key, value in bucket.items():
                all_values.append(value)
        # Returns list of of all values
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table."""
        """Running time: O(n) for loop iterates through buckets"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets."""
        """Running time: O(1) returns size attribute"""
        return self.size
        
    def contains(self, key):
        """Return True if this hash table contains the given key, or False."""
        """Running time: O(n) used find method"""
        # Get bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Returns boolean of if key-value entry exists in bucket
        return bucket.find(lambda key_value: key_value[0] == key) is not None
        

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError."""
        """Running time: O(n) used find method"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket
        value = bucket.find(lambda key_value: key_value[0] == key)
        # If found, return value associated with given key
        if value is not None:
            return value[1]
        else:
            raise KeyError('Key not found {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value."""
        """Running time: O(n) used find method"""

        # ATTEMPT #1

        # # Find bucket where given key belongs
        # index  = self._bucket_index(key)
        # bucket = self.buckets[index]
        # value  = bucket.find(lambda key_value: key_value[0] == key)
        # # Check if key-value entry exists in bucket
        # if value == None:
        #     # If not found, insert given key-value entry into bucket
        #     entry = (key, value)
        #     bucket.append(entry)
        #     self.size += 1
        # else:
        #     # If found, update value associated with given key
        #     bucket.replace(value, (key, value))

        # ATTEMPT #2

        # Find bucket where given key belongs
        index = self._bucket_index(key)
        buck = self.buckets[index]
        found_item  = buck.find(lambda entry: entry[0] == key)
        # Check if key-value entry exists in bucket
        if found_item is not None:
            # If found, update value associated with given key
            buck.replace(found_item, (key, value))
        else:
            # If not found, insert given key-value entry into bucket
            buck.append((key, value))
            self.size += 1

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError."""
        """Running time: O(n) used find method"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        value  = bucket.find(lambda key_value: key_value[0] == key)
        # Check if key-value entry exists in bucket
        if value == None:
            # If not, raise error to tell user delete failed
            raise KeyError('Key not found {}'.format(key))
        else:
            # If found, delete entry associated with given key
            bucket.delete(value)
            self.size -=1

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()