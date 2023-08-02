
# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        slow,fast = nums[0],nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast: break
        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
    
s=Solution()
print(s.findDuplicate([1,3,4,2,2]))
