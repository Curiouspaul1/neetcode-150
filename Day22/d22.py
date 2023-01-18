# loop through the stack
# check 

def revRPN(tokens):
    stack = []
    for c in tokens:
        if c == "+":
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(a + b)
        elif c == "-":
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(b - a)
        elif c == "*":
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(a * b)
        elif c == "/":
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(int(b / a))
        else:
            stack.append(int(c))

    return stack[0]

tokens = ["4","13","5","/","+"]
#print(revRPN(tokens))
print(int(tokens[0]) + int(tokens[1]))
