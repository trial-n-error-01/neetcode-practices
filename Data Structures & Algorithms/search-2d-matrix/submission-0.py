class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        def binary(nums, left, right):
            if(left>right):
                return False
            nonlocal target
            mid = left + (right - left) // 2

            if(nums[mid]== target):
                return True
            elif(nums[mid]<target):
                return binary(nums, mid+1, right)
            else:
                return binary(nums, left, mid-1)
        
            return binary(0, len(nums) - 1)      

        for i in matrix:
            if binary(i,0, len(i)-1):
                return True
        
        return False