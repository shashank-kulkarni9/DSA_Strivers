
#https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        x = 1   # ROW
        y = 1   # COL

        # Check for zeros in the first row
        for j in range(n):
            if matrix[0][j] == 0:
                x = 0

        # Check for zeros in the first column
        for i in range(m):
            if matrix[i][0] == 0:
                y = 0

        # Identify zero positions and store in the first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Apply zeros based on the first row and first column information
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Update the first row
        if y == 0:
            for i in range(m):
                matrix[i][0] = 0

        # Update the first column
        if x == 0:
            for j in range(n):
                matrix[0][j] = 0
        return matrix
        
s=Solution()
arr=s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
print(arr)