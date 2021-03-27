class Solution:
    def mark_island(self, x: int, y: int, r: int, c: int, grid: List[List[int]]) -> int:
        num_of_land = 0
        if x<0 or x>= r or y<0 or y>= c or grid[x][y] != 1:
            return num_of_land
        
        grid[x][y] = 2
        num_of_land +=1
        
        #cover all land
        num_of_land += self.mark_island(x+1,y,r,c,grid) #move down
        num_of_land += self.mark_island(x-1,y,r,c,grid) #move up
        num_of_land += self.mark_island(x,y+1,r,c,grid) #move right
        num_of_land += self.mark_island(x,y-1,r,c,grid) #move left
        
        return num_of_land
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_land = 0
        
        r = len(grid)
        if r == 0:
            return 0
        c = len(grid[0])
        
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 1:
                    num_land = self.mark_island(x,y,r,c,grid)
                    max_land = max(max_land, num_land)
                    
        return max_land