from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_array = sorted(nums)
        
        front = 0
        back = len(nums) - 1

        
        while True:
            s = sorted_array[front] + sorted_array[back]
            
            if s == target:
                result = []
                for index, _ in enumerate(nums):
                    if nums[index] == sorted_array[front] or nums[index] == sorted_array[back]:
                        result.append(index)
                return result
                
            elif s > target:
                back -= 1
            else:
                front += 1
        