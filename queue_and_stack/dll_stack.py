from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        return True

    def pop(self):
        if self.len() > 0:
            return self.storage.remove_from_head()
        return None

    def len(self):
        return len(self.storage)
