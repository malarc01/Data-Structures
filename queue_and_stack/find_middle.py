from doubly_linked_list import DoublyLinkedList

# return the middle node of the DLL, if there are two nodes, return the left one

# no empty list , length >= 1
# not sorted
# we do not know length!
# only one pass through

# 1-2-3: 2
# 5-2-3-5: 2

# Understand - not sorted

# Plan:
# - floor division
# - get length by travering it
# - traverse until length/2

# - which direction?
# - forwards
# - backwards


def find_middle(dll):
    head = dll.head
    tail = dll.tail

    while head != tail and head.next != tail:
        head = head.next
        tail = tail.prev

    return head.value


odd_nums = DoublyLinkedList()
[odd_nums.add_to_head(i) for i in[5, 3, 4, 10, 7]]
print(find_middle(odd_nums))

even_nums = DoublyLinkedList()
[even_nums.add_to_tail(i) for i in [5, 3, 4, '10', 7, 8, ]]
print(find_middle(even_nums))

ians_nums = DoublyLinkedList()
[ians_nums.add_to_head(i) for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(find_middle(ians_nums))

list_1 = DoublyLinkedList()
list_1.add_to_head(10)
print(find_middle(list_1))

list_2 = DoublyLinkedList()
list_2.add_to_head(10)
list_2.add_to_head(11)
print(find_middle(list_2))

really_long_list = DoublyLinkedList()
[really_long_list.add_to_head(i) for i in range(1, 1000000)]
print(find_middle(ians_nums))
