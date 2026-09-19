class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
            buckets = [ [] for _ in range(len(nums) +1) ]
            countHashMap = {}
            for num in nums:
                countHashMap[num] = countHashMap.get(num,0)+1
            
            for i,v in countHashMap.items():
                buckets[v].append(i)

         #   print(buckets)
            
            ans = []
            for bucket in buckets[::-1]:
                if(bucket!=[]):
                    ans+=(bucket)
                if(len(ans)==k):
                    break

            return ans
