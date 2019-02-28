#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0     # Length of linked list
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty.
        Running time: O(1)"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(1) used size property"""
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) - Only if statements used"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new = Node(item)
        self.size += 1

        if self.is_empty():
            self.head = new
            self.tail = new
        
        else:
            self.tail.next = new
            self.tail = new
            

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1)"""

        # Create new node to hold given item
        new = Node(item)
        self.size += 1

        # If empty it initializes a linked list
        if self.is_empty():
            self.head = new
            self.tail = new

        else:
            # Prepend node before head, if it exists
            new.next = self.head
            self.head = new


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        
        # ATTEMPT #1
        # current = self.head
        # while current != None:
        #     if quality(current.data):
        #         return current.data
        #     current = current.next

        # return None

        # ATTEMPT #2
        # https://stackoverflow.com/questions/46656563/how-to-debug-typeerror-str-object-is-not-callable-python3-when-implementing-li
        # current = self.head
        #     # Loop through all nodes 
        #     # find item where quality(item) is True
        #     while not quality(current.data):
        #         # Check if node's data satisfies given quality function
        #         if current.next == None:
        #             return None
        #         else:
        #             # Files to next node
        #             current = current.next

        # ATTEMPT #3
        # Optimize for empty linked list
        if self.is_empty():
            return None

        # Optimize for head
        if quality(self.head.data):
            return self.head.data

        # Optimize for tail
        if quality(self.tail.data):
            return self.tail.data

        else:
            node = self.head

            # Loop through all nodes
            while node is not None:
                # find item where quality(item) is True
                if quality(node.data):
                    return node.data
                # Files to next node
                node = node.next

            return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) when item is head
        Worst case running time: O(n) when item has to be found"""

        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        else:

            # if item is head node
            if item == self.head.data:
                # subtract node from size when match found
                self.size -= 1

                if self.head.next == None:
                    self.tail = None
                # set head to next node
                self.head = self.head.next
                return
            
            # Loops through all nodes to find one whose data matches given item
            previous = self.head
            current  = self.head.next
            while current is not None:
                if item == current.data:
                    # subtract node from size when match found
                    self.size -= 1

                    # changes previous node next arrow to point to the node after current
                    # current node is then lost due to pythons garbage collection
                    previous.next = current.next

                    if previous.next is None:
                        self.tail = previous
                    return

                    if self.head == None:
                        self.tail = None
                    return

                # traversal
                previous = current
                current = current.next

            raise ValueError('Item not found: {}'.format(item)) 


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()