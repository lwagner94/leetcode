from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
            
        combinations = []
        
        for digit in digits:
            new_combinations = []
            for letter in letter_map[int(digit)]:
                for combo in combinations:
                    new_combinations.append(combo + letter)
                if len(combinations) == 0:
                    new_combinations.append(letter)
            combinations = new_combinations
            
        return combinations
        