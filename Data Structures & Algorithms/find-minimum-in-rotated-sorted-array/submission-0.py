class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l , r = 0, len(nums)-1

        while(l<=r):        

            if(nums[l]<nums[r]):
                minimum = min(minimum, nums[l])
                break
            
            mid= (r+l)//2;
            minimum = min(minimum, nums[mid])
            if(nums[l]<=nums[mid]):
                l = mid+1
            else:
                r= mid-1

        return minimum