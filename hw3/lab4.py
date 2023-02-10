Operators = set(['+', '-', '*', '/', '(', ')'])

myInPut = '(A+B)*C-D*F+C'


def iToF(myInPut):
    stack = []
    output = ''

    for inp in myInPut:

        if inp == '(':
            stack.append('(')

        elif inp == ')':
            while stack[-1] != '(':
                output = output+stack.pop()
            stack.pop()

        elif inp not in Operators:
            output = output+inp

        elif inp == '+' or '-' and stack and stack[-1] != '(' and stack and stack[-1] == '*' and '/' and '+' and '-':
            while stack and stack[-1] != '(':
                output = output+stack.pop()
            stack.append(inp)

        elif inp == '-' or '+' and stack and stack[-1] != '(' and stack and stack[-1] == '*' and '/' and '+' and '-':
            while stack and stack[-1] != '(':
                output = output+stack.pop()
            stack.append(inp)

        elif inp == '*' or '/' and stack and stack[-1] != '(' and stack and stack[-1] == '+' and '-':
            stack.append(inp)

        elif inp == '/' or '*' and stack and stack[-1] != '(' and stack and stack[-1] == '+' and '-':
            stack.append(inp)

    while stack:
        output += stack.pop()

    return output


print(iToF(myInPut))
