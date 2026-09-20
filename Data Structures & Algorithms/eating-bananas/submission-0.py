class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary with left minimum speed 1 and right -> max piles

        left, right = 1, max(piles)
        minimumSpeed =  right

        while(left<=right):
            kMid = (right+left)//2

            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p)/kMid)

            if totalTime <=h :
                minimumSpeed = kMid
                right = kMid - 1
            else:
                left = kMid +1
        
        return minimumSpeed