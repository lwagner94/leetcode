def up_down(to_excl: int):
    while True:
        for i in range(to_excl):
            yield i

        for i in range(to_excl - 2, 0, -1):
            yield i


class Solution:
    def convert(self, s: str, numRows: int) -> str:      
        lines = ["" for _ in range(numRows)]
        for c, current_line in zip(s, up_down(numRows)):
            lines[current_line] += c

        return "".join(lines)


s = Solution()

result = s.convert("PAYPALISHIRING", 3)
print(result)

result = s.convert("PAYPALISHIRING", 4)
print(result)


result = s.convert("AB", 1)
print(result)