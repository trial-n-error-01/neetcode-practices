class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        buckets = [[] for _ in range(len(nums)+1)]

        for  val in nums:
            count[val]= count.get(val,0)+1
        

        for index, val in count.items():
            buckets[val].append(index)
        
        ans =[]
        for freq in buckets[::-1]:
            if(freq!=[]):
                ans+=freq
            if(len(ans)==k):
                break
        
        return ans

