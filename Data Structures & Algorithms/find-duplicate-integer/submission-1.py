class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # can be done 3 ways
        # Bit manipulation
        # Negative indexation
        # fast and slow pointers

        for number in nums:
            idx = abs(number) - 1
            if nums[idx] < 0:
                return abs(number)
            nums[idx] *= -1
        return -1
