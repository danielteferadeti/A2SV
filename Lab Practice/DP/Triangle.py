class Solution:
    
    def recSol(self, row: int,  index: int,triangle: List[List[int]], memo: dict) -> int:
        
        if (row, index) in memo:
            return memo[(row,index)]
        
        cur = triangle[row][index]
        if row == len(triangle) - 1:
            return cur
        
        left = self.recSol(row +1, index, triangle, memo)
        right = self.recSol(row+1, index +1, triangle, memo)
        
        cur += min(left,right)
        memo[(row,index)] = cur
        return cur
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = dict()

        return self.recSol(0,0,triangle,memo)
    
        # return self.B_up(triangle)
        
    def B_up(self, triangle: List[List[int]]):
        minArr = triangle[len(triangle) - 1]
        
        i = len(triangle) - 2
        while i >-1:
            givenList = triangle[i]
            # print(givenList)
            for j in range(len(givenList)):
                if minArr[j] < minArr[j +1]:
                    minArr[j] = givenList[j] + minArr[j]
                else:
                    minArr[j] = givenList[j] + minArr[j +1]
                # print(minArr)
            i -= 1
        return minArr[0]
