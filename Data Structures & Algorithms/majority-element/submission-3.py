class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #same loop
        #28 ms
        hashMap = defaultdict(int)
        ans, maxC = 0,0
        for number in nums:
            hashMap[number] = hashMap.get(number,0)+1
            if(maxC<hashMap[number] ):
                maxC= hashMap[number] 
                ans = number
        
        return ans