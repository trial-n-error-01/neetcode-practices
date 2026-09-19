class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        leftIndex, rightIndex = 0 , len(height)-1
        maxWater = 0
        while (leftIndex<rightIndex):
            
            waterCurrent = min(height[leftIndex], height[rightIndex])*(rightIndex-leftIndex)
            maxWater = max(maxWater, waterCurrent)
            if(height[leftIndex]>=height[rightIndex]):
                rightIndex-=1
            else:
                leftIndex+=1
        
        return maxWater