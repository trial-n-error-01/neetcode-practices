class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # can be done 3 ways
        # Bit manipulation
        # Negative indexation
        # fast and slow pointers

# Phase 1: Find the intersection point of the two runners in the cycle
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]          # Move 1 step
            fast = nums[nums[fast]]    # Move 2 steps
            if slow == fast:
                break
                
        # Phase 2: Find the "entrance" to the cycle (the duplicate number)
        slow = nums[0]                 # Reset slow to the start
        while slow != fast:
            slow = nums[slow]          # Move 1 step
            fast = nums[fast]          # Move 1 step
            
        return slow                    # They meet at the duplicate

        # 93 ms