class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setVersion = set(nums)
        return len(nums)!=len(setVersion)