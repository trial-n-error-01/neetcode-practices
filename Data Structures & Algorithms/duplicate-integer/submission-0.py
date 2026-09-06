class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in nums:
            hashMap[i]= hashMap.get(i,0)+1
            if(hashMap[i])>1:
                return True
        
        return False