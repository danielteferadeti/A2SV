class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = []
        visited = []
        colLen = len(isWater[0])
        rowLen = len(isWater)
        
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    queue.append((i,j,0))
                    visited.append((i,j))
        while queue:
            i,j, height  = queue.pop(0)

            isWater[i][j] = height
            #Move up 
            if i - 1 >=0 and (i-1,j) not in visited:
                queue.append((i-1,j,height+1))
                visited.append((i-1,j))
            #Move down
            if i + 1 < rowLen and (i+1,j) not in visited:
                queue.append((i+1,j,height+1))
                visited.append((i+1,j))
            #Move to Left
            if j - 1 >= 0 and (i,j-1) not in visited:
                queue.append((i,j-1,height+1))
                visited.append((i,j-1))
            #Move to Right
            if j + 1 < colLen and (i, j+1) not in visited:
                queue.append((i,j+1,height+1))
                visited.append((i,j+1))
        return isWater