
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        lo = 0
        if not matrix:
            return False
        hi = (len(matrix) * len(matrix[0])) - 1

        while lo <= hi:
            mid = (lo + (hi - lo) // 2)
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target:
                return True
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
    

s=Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))