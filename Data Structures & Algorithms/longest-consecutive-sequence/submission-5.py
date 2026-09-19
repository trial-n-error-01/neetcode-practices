class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestStreak = 0
        uniqueNums = set(nums)

        for number in nums:
            if(number-1 not in uniqueNums):
                streak = 1
                currentNum= number
                while (currentNum+ 1) in uniqueNums:
                    streak+=1
                    currentNum+=1
                longestStreak = max(streak, longestStreak)
        
        return longestStreak