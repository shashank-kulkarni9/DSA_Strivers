
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m+n-1
        
        while(n>0):
            if(m>0 and nums1[m-1]>nums2[n-1]):
                nums1[index] = nums1[m-1]
                m-=1
            
            else:
                nums1[index] = nums2[n-1]
                n-=1
            
            index-=1
        return nums1

s=Solution()
print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))