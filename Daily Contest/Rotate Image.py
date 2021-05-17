class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Use Transpose function
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # print("i = " + str(i) + " j = " + str(j))
                if (i,j) not in visited and (j,i) not in visited:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                    visited.add((i,j))
                    visited.add((j,i))
        ##############
        # print(matrix)
        for k in range(len(matrix)):
            ptr1,ptr2 = 0,len(matrix[0])-1
            while ptr1 != ptr2 and ptr1 < ptr2:
                temp = matrix[k][ptr1]
                matrix[k][ptr1] = matrix[k][ptr2]
                matrix[k][ptr2] = temp
                ptr1 +=1
                ptr2 -=1