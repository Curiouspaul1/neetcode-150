def generateParenthesis(n):
    stack = []
    res = []

    def backtract(openN, closeN):
        if openN == closeN == n:
            res.append("".join(stack))
            return
        
        if openN < n:
            stack.append("(")
            backtract(openN + 1, closeN)
            stack.pop()
        
        if closeN < openN:
            stack.append(")")
            backtract(openN, closeN + 1)
            stack.pop()

    
    backtract(0, 0)
    return res

n = 3

print(generateParenthesis(n))
