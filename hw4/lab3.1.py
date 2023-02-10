class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.poiter = None


class SLinkedList:
    def __init_(self):
        self.header = None


list = SLinkedList()

e1 = Node("44")
e2 = Node("36")
e3 = Node("90")
e4 = Node("10")
e5 = Node("60")
e6 = Node("99")

list.header = e1
e1.poiter = e2
e2.poiter = e3
e3.poiter = e4
e4.poiter = e5
e5.poiter = e6
