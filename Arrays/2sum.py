
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, lst: [int], k: int) -> [int]:
        d={}
        for i in range(len(lst)):
            r=k-lst[i]
            if r in d:
                return [d[r], i]
            d[lst[i]]=i
        return [-1,-1]

s=Solution()
print(s.twoSum([2,7,11,15],9))