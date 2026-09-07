class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        
        p = 1
        for i in nums:
            if i != 0:
                p *= i
        
        ans = []
        for i in nums:
            if zero_count == 1:
                ans.append(p if i == 0 else 0)
            else:
                ans.append(p // i)

        return ans