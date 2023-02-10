class Node:
    def init__(self, dataval=None):

        self.dataval = dataval
        self.left = None
        self.right = None


class SLinkedList:

    def __init_(self):

        self.header = None


list = SLinkedList()

e1 = Node("1")

e2 = Node("2")

e3 = Node("3")

e4 = Node("4")

list.header = e1

e1.right = e2

e2.left = e1

e2.right = e3

e3.left = e2

e3.right = e4

e4.left = e3
