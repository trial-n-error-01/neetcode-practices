class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # Array of lists to store numbers by their frequency
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Step 1: Count frequency of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # Step 2: Map frequency to list of numbers
        for n, c in count.items():
            freq[c].append(n)
            
        # Step 3: Gather top k elements starting from the highest frequency
        res = []
        counter= 0
        while(len(res)<k):
            res+=freq[-1-counter]
            counter+=1

        return res