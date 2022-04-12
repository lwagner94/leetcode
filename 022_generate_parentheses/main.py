from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def gen(current, depth, nesting) -> List[str]:
            if nesting > n or nesting < 0 or current.count("(") > n:
                return []
            if depth == n * 2:
                return [current]
            
            left = gen(current + "(", depth + 1, nesting + 1)
            right = gen(current + ")", depth + 1, nesting - 1)
            
            return left + right
            
        return gen("(", 1, 1)
    
        