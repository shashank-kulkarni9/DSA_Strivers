
# KADANES ALGO
# https://leetcode.com/problems/maximum-subarray/

import sys
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        maxi = -sys.maxsize-1
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            maxi=max(s,maxi)
            if s<0: s=0
        return maxi
    
s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
