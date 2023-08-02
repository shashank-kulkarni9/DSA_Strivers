
# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, a):
        n = len(a) 
        SN = (n * (n + 1)) // 2
        S2N = (n * (n + 1) * (2 * n + 1)) // 6
        S, S2 = 0, 0
        for i in range(n):
            S += a[i]
            S2 += a[i] * a[i]

        # S-Sn = X-Y:
        val1 = S - SN

        # S2-S2n = X^2-Y^2:
        val2 = S2 - S2N

        # Find X+Y = (X^2-Y^2)/(X-Y):
        val2 = val2 // val1

        # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
        # Here, X-Y = val1 and X+Y = val2:
        x = (val1 + val2) // 2
        y = x - val1

        return [x, y]
    
   
s=Solution()
print(s.repeatedNumber([3 ,1, 2, 5, 3])) 
