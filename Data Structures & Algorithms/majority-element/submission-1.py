class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #28 ms
        hashMap = defaultdict(int)
        for number in nums:
            hashMap[number] = hashMap.get(number,0)+1

        for number in hashMap:
            if(hashMap[number]>=(len(nums)//2)):
                return number
        
        return 0