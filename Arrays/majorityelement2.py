
# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: [int]) -> [int]:

        # moore's voting algo ext
        n=len(nums)
        c1,c2=0,0
        ele1,ele2=None,None
        for i in range(n):
            if c1==0 and ele2!=nums[i]:
                c1=1
                ele1=nums[i]
            elif c2==0 and ele1!=nums[i]:
                c2=1
                ele2=nums[i]
            elif ele1==nums[i]:
                c1+=1
            elif ele2==nums[i]:
                c2+=1
            else:
                c1-=1
                c2-=1
        l=[]
        c1,c2=0,0
        for i in nums:
            if i==ele1: c1+=1
            if i==ele2: c2+=1
        mini=n/3
        if c1>mini: l.append(ele1)
        if c2>mini: l.append(ele2)
        return l
    
s = Solution()
print(s.majorityElement([11, 33, 33, 11, 33, 11]))