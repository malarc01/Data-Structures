from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # self.head = None
        # self.tail = None
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.storage.add_to_tail(value)

        # new_node = DoublyLinkedList(value)
        # if self.head == None:
        #     self.head = self.tail = new_node
        # else:
        #     self.tail.next = new_node
        #     new_node.previous = self.tail
        #     self.tail = new_node
        # self.size += 1

    def dequeue(self):

        return self.storage.remove_from_head()

        # value = self.head
        # self.head = self.head
        # self.size -= 1
        # if self.size == 0:
        #     self.tail = 0
        # return value

    def len(self):
        return self.storage.length
