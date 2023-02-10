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


def lastNodeDel(root, myLastNode):
    myQueue = []
    myQueue.append(root)
    while (len(myQueue)):
        temp = myQueue.pop(0)
        if temp is myLastNode:
            temp = None
            return
        if temp.right:
            if temp.right is myLastNode:
                temp.right = None
                return
            else:
                myQueue.append(temp.right)
        if temp.left:
            if temp.left is myLastNode:
                temp.left = None
                return
            else:
                myQueue.append(temp.left)


def delNode(root, delTarget):
    if root == None:
        return None
    if root.left is None and root.right is None:
        if root.data == delTarget:
            temp = root.right
            root = None
            return temp
    delTarget_node = None
    myQueue = []
    myQueue.append(root)
    temp = None
    while (len(myQueue)):
        temp = myQueue.pop(0)
        if temp.data == delTarget:
            delTarget_node = temp
        if temp.left:
            myQueue.append(temp.left)
        if temp.right:
            myQueue.append(temp.right)
    if delTarget_node:
        lastNodeVal = temp.data
        lastNodeDel(root, temp)
        delTarget_node.data = lastNodeVal
    return root


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


def myDel(root):
    while (1):
        delTarget = int(input('Del Node: '))
        root = delNode(root, delTarget)
        print2DTree(root)


def myAdd():
    while (1):
        myNode = input('Add Node:')
        if myNode.isdigit():
            root.insert(int(myNode))
            myAdd()
        else:
            myDel(root)


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
