class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')': 
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif c == '[':
                stack.append(c)
            elif c == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif c == '{':
                stack.append(c)
            elif c == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0