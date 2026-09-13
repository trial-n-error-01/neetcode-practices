class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,v in enumerate(numbers):
            if (target-v) in hashMap:
                return [hashMap[target-v]+1, i+1]
            hashMap[v]=i
        
        return []