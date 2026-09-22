class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # can be done 3 ways
        # Bit manipulation
        # Negative indexation
        # fast and slow pointers
        n = len(nums) - 1
        ans = 0
        
        # Check each bit position from 0 to 31
        for i in range(32):
            bit = 1 << i
            base_count = 0
            nums_count = 0
            
            # 1. Count how many numbers from 1 to n have this bit set
            for k in range(1, n + 1):
                if k & bit:
                    base_count += 1
                    
            # 2. Count how many numbers in nums have this bit set
            for num in nums:
                if num & bit:
                    nums_count += 1
                    
            # 3. If nums has more, the duplicate has this bit
            if nums_count > base_count:
                ans |= bit
                
        return ans
        
