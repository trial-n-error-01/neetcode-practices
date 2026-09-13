class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        longest_streak = 0

        for num in nums:
            if not hashMap[num]:
                hashMap[num] =hashMap[num - 1] + hashMap[num + 1] + 1
                hashMap[num - hashMap[num - 1]] = hashMap[num]
                hashMap[num + hashMap[num + 1]] = hashMap[num]
                longest_streak = max(longest_streak, hashMap[num])
        return longest_streak
