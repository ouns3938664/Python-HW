import collections


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    print2DTree(root)

                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                    print2DTree(root)

                else:
                    self.right.insert(data)


def print2DTree(root, space=0, LEVEL_SPACE=5):
    if (root == None):
        return
    space += LEVEL_SPACE
    print2DTree(root.right, space)
    # print() # neighbor space
    for i in range(LEVEL_SPACE, space):
        print(end=" ")
    print("|" + str(root.data) + "|<")
    print2DTree(root.left, space)


def myAdd():
    while (1):
        myNode = input('Add Node:')
        if myNode.isdigit():
            root.insert(int(myNode))
            myAdd()
        else:
            print('Only INT!')


while (1):
    myRoot = input('Add Root:')
    if myRoot.isdigit():
        root = Node(int(myRoot))
        print2DTree(root)
        myAdd()
    else:
        print('Only INT!')
while (1):
    myAdd()
