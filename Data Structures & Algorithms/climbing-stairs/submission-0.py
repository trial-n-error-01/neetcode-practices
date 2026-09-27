class Solution:
    def climbStairs(self, n: int) -> int:
        
        # mathematical intution

        sqrtOfFive = math.sqrt(5)
        phi = (1 + sqrtOfFive) / 2
        psi = (1 - sqrtOfFive) / 2
        n +=1

        return round((phi**n - psi**n)/sqrtOfFive)