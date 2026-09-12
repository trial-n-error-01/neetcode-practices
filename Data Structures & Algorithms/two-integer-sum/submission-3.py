#Complexity of this one is O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        keyValPairs={}

        for key, value in enumerate(nums):
            
            if(target-value) in keyValPairs:
                return [ keyValPairs[target-value], key]

            keyValPairs[value]= key
        
