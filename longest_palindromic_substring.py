#!/usr/bin/env python3

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l_start = 0
        l_end = 0



        for i in range(len(s)):
            start = i

            # if len(s) % 2 == 1:
            #     end = i
            # else:
            #     end = i + 1

            end = i

            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    if (end - start + 1) > (l_end - l_start + 1):
                        l_end = end
                        l_start = start


                    start -= 1
                    end += 1
                else: 
                    break
        
        return s[l_start:l_end+1]



        

s = Solution()

assert s.longestPalindrome("baaa") == "aaa"
assert s.longestPalindrome("aaa") == "aaa"
assert s.longestPalindrome("a") == "a"
assert s.longestPalindrome("faad") == "aa"
assert s.longestPalindrome("faaad") == "aaa"
assert s.longestPalindrome("ffad") == "ff"
assert s.longestPalindrome("fffad") == "fff"

print(result)