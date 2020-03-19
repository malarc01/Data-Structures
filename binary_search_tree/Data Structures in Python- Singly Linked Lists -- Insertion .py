class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        # if node already exist
        print('SELF.HEAD', self.head)

        last_node = self.head
        print('last_node', last_node)
        print('SELF.HEAD', self.head)

        while last_node.next:
            print('XLSOSO')
            last_node = last_node.next

        print('last_node.next', last_node.next)
        last_node.next = new_node
        print('last_node.next==>', last_node.next)

    def prepend(self, data):
        new_node = Node(data)
        print(new_node)
        print('self.head', self.head)
        new_node.next = self.head
        print('before self.head ==>', self.head)
        self.head = new_node
        print('after self.head ==>', self.head)


linked_list = LinkedList()
linked_list.append('Human')
linked_list.append('Pineapple')
# linked_list.append('Apple')
# linked_list.append('Banana')
# linked_list.prepend('Dog')
linked_list.print_list()
