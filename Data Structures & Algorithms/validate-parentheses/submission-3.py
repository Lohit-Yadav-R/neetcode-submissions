class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {']' : '[', '}' : '{', ')' : '('}
        for _ in s:
            if _ in closeToOpen:
                if stack and closeToOpen[_] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(_)
        return True if not stack else False