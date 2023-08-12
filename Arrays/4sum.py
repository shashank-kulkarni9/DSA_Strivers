class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        n = len(nums)
        nums.sort()
        ans=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]: continue
            for j in range(i+1,n):
                if j>(i+1) and nums[j]==nums[j-1]: continue
                k,l=j+1,n-1
                while k<l:
                    sum = nums[i]+nums[j]+nums[k]+nums[l]
                    if sum==target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]: k+=1
                        while k<l and nums[l]==nums[l+1]: l-=1
                    elif sum<target: k+=1
                    else: l-=1
        return ans
    
s=Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))