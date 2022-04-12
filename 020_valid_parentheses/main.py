from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                stack_top = stack.pop()
                if (ord(c) - ord(stack_top)) not in (1,2):

                    return False
        return len(stack) == 0