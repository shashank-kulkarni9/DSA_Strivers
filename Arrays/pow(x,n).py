
# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # strivers
        p = 1
        f=0
        if n<0:
            f=1
            n=(-1*n)
        while n:
            if n%2:
                p = p*x 
                n-=1
            else:
                x = x*x
                n=n//2
        if f: return (1/p)
        return p
    
s=Solution()
print(s.myPow(2.00000,10))