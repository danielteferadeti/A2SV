class Solution:   
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        
        rw,cln = len(matrix), len(matrix[0])
        memoMatrix = [[0]*cln for i in range(rw)]
        
        def isValid(i,j):
            if i < 0 or i>=rw or j<0 or j>=cln:
                return False
            return True
    
        def dfs(i,j):
            if memoMatrix[i][j] ==0:
                possibleMaxims = []
                for rw_d, cln_d in ((i,j-1), (i,j+1), (i-1,j),(i+1,j)):
                    if isValid(rw_d, cln_d) and matrix[rw_d][cln_d] > matrix[i][j]:
                        possibleMaxims.append(dfs(rw_d,cln_d))
                memoMatrix[i][j] = 1 + max(possibleMaxims, default=0)
            return memoMatrix[i][j]
        
        return max(dfs(i,j) for i in range(rw) for j in range(cln))