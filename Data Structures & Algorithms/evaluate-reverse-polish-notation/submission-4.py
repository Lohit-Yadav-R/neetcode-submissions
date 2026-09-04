class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    item2 = stack.pop()
                    item1 = stack.pop()
                    stack.append(item1 + item2)
                case '-':
                    item2 = stack.pop()
                    item1 = stack.pop()
                    stack.append(item1 - item2)
                case '*':
                    item2 = stack.pop()
                    item1 = stack.pop()
                    stack.append(item1 * item2)
                case '/':
                    item2 = stack.pop()
                    item1 = stack.pop()
                    stack.append(int((item1 / item2)))
                case _:
                    stack.append(int(token))
        
        return stack.pop()