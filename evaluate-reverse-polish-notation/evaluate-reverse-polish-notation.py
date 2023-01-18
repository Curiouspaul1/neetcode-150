class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = { "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: x / y,
              }
        i = 0
        
        while len(tokens) > 1:
            if tokens[i] in ops.keys():
                ops_res = ops[tokens[i]](int(tokens[i-2]), int(tokens[i-1]))
                tokens[i-2] = ops_res
                del tokens[i]
                del tokens[i-1]
                i = 0
            else:
                i += 1
        return int(tokens[0])
            
        s