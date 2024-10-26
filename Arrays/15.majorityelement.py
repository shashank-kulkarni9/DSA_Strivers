
# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: [int]) -> int:

        # Moores voting algo
        n=len(nums)
        cnt = 0
        for i in range(n):
            if cnt==0:
                cnt=1
                ele = nums[i]
            elif nums[i]==ele:
                cnt+=1
            else: cnt-=1
        if nums.count(ele)>n/2:
            return ele
        return -1
    
s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))