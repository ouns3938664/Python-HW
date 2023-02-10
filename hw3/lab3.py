myInPut = 'ABCDEF'


def myStack(myInPut):
    stack = []
    outputStack = []
    for inp in myInPut:
        stack. append(inp)

    while stack:

        output = stack.pop()
        outputStack. append(output)

    return outputStack


print(myStack(myInPut))
