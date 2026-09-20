class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0

        for bit in range(32):
            count = 0

            for number in nums:
                if number & (1 << bit):
                    count += 1

            if count > len(nums) // 2:
                result |= 1 << bit

        # Convert 32-bit two's-complement result to Python's negative integer
        if result >= 1 << 31:
            result -= 1 << 32

        return result