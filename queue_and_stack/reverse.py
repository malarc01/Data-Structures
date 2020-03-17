from doubly_linked_list import DoublyLinkedList

# no recursion
# we cannot store the DLL and its data in other data structures


def reverse(dll):
    current = dll.head
    # this will be our new tail
    new = current.next
    current.next = None

    while new is not None:
        prev = current
        current = new
        current.next = prev
        # move on
        new = current.next

