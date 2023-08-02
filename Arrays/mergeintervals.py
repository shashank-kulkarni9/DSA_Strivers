
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, arr):
        n = len(arr)
        arr.sort()
        res = []
        for i in range(n):
            if not res or arr[i][0]>res[-1][1]:
                res.append(arr[i])
            else:
                res[-1][1]=max(res[-1][1],arr[i][1])
        return res
    
s=Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))