# from dll_stack import Stack
# from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')

# TreeNode


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None  # BinarySearchTree
        self.right = None  # BinarySearchTree

    # Insert the given value into the tree
    def insert(self, value):

        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return

        if value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)
        # compare value to the current node
        # if smaller,go left
        # if bigger, go right

        # if no node to go to, (either left or right)
            # make the new node at that spot

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if target == self.value:
            return True

        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)

        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

        # compare value to the current node value
        # if smaller, go left
        # if bigger, go right

        # if equal, return True!

        # if smaller, but can NOT go left, return False
        # if bigger,but we can NOT go right, return False

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # go left FIRST
        if self.left is not None:
            self.left.for_each(cb)
        # print ourselves
        cb(self.value)

        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
         # go left FIRST
        if node.left is not None:
            node.left.in_order_print(node.left)

        # print ourselves
        print(node.value)
        if node.right is not None:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # create a queue for nodes
        # add current node to queue
        # while the queue is not empty:
        # dequeue a node
        # print the node
        # add its children
        # i.e  add left(if you can)
        # add right (if you can )

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    def dft_print(self, node):
        pass
        # create a node_stack

        # push the current node onto stack

        # while we have items on stack

        # print the current value and pop it off

        # push the right value of the current node if we can

        # push the left value of current node if we can

        # STRETCH Goals -------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(12)
bst.insert(9)
bst.insert(7)
bst.insert(13)
bst.insert(14)
bst.insert(17)

bst.for_each(print)
