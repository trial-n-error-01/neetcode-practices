from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sorting is essential for the two-pointer approach
        
        for i in range(len(nums)):
            # Skip duplicate elements for the first number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total > 0:
                    right -= 1  # Sum is too large, move right pointer down
                elif total < 0:
                    left += 1   # Sum is too small, move left pointer up
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers inward
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res