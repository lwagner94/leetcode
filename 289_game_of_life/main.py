from typing import List
from copy import deepcopy

class Solution:
    
    def lookup(self, board: List[List[int]], x: int, y: int) -> int:
        if x < 0 or y < 0:
            return 0

        width = len(board[0])
        height = len(board)

        if x >= width or y>=height:
            return 0

        return board[y][x]

    def determineNumberOfAliveNeighbors(self, board: List[List[int]], x: int, y: int) -> int:
        alive = 0

        for y_offset in (-1, 0, 1):
            for x_offset in (-1, 0, 1):
                if y_offset == 0 and x_offset == 0:
                    continue

                alive += self.lookup(board, x + x_offset, y + y_offset)
        
        return alive
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        old = deepcopy(board)
        
        width = len(board[0])
        height = len(board)
        

        for y in range(height):
            for x in range(width):
                alive = self.determineNumberOfAliveNeighbors(old, x, y)

                if alive < 2 or alive > 3:
                    board[y][x] = 0
                elif alive == 3:
                    board[y][x] = 1
                else:
                    board[y][x] = old[y][x]
        


s = Solution()

board = [[1,1],[1,0]]
s.gameOfLife(board)


print(board)