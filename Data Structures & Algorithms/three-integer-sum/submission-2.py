from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        duplicates = set()
        
        for i, val1 in enumerate(nums):
            # Optimization: Skip if we've already processed this exact outer number
            if val1 not in duplicates:
                duplicates.add(val1)
                seen = {}
                
                for j in range(i + 1, len(nums)):
                    val2 = nums[j]
                    complement = -val1 - val2
                    
                    if complement in seen:
                        # Found a triplet! Sort it so [a, b, c] and [b, a, c] 
                        # are recognized as the same set by our 'res' hash set.
                        triplet = tuple(sorted([val1, val2, complement]))
                        res.add(triplet)
                        
                    seen[val2] = j
                    
        return [list(triplet) for triplet in res]