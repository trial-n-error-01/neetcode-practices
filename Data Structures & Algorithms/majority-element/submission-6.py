class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Bitwise version
        n = len(nums)
        bit = [0] * 32
        for num in nums:
            for i in range(32):
                bit[i] += ((num >> i) & 1)

        res = 0
        for i in range(32):
            if bit[i] > (n // 2):
                if i == 31:
                    res -= (1 << i)
                else:
                    res |= (1 << i)
        return res