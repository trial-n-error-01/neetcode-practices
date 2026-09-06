class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(left, right):
            if(left>right):
                return -1
            nonlocal target
            mid = left + (right - left) // 2

            if(nums[mid]== target):
                return mid
            elif(nums[mid]<target):
                return binary(mid+1, right)
            else:
                return binary(left, mid-1)
        
        return binary(0, len(nums) - 1)        


