
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int):
        final = []
        for row in range(1,numRows+1):
            temp = []
            res = 1
            temp.append(res)
            for i in range(1,row):
                res = res*(row-i)//i
                temp.append(res)
            final.append(temp)
        return final

s=Solution()
print(s.generate(5))
