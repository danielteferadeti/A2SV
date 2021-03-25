import sys
class Solution:
    
    def recSol(self, row: int, index:int, grid: List[List[int]], memo)-> int:
        
        if (row,index) in memo:
            return memo[(row,index)]
        
        #Check Validity
        if row > len(grid) -1:
            return sys.maxsize -1
        
        if index > len(grid[0]) -1:
            return sys.maxsize -1
        
        #Base Case
        if row == len(grid) -1:
            if index == len(grid[row]) -1:
                return grid[row][index]

        cur = grid[row][index]
        
        right = self.recSol(row,index + 1,grid,memo)
        down = self.recSol(row+1,index, grid,memo)
        
        cur += min(right,down)
        memo[(row,index)] = cur
        return cur
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = dict()
        return self.recSol(0,0,grid,memo)