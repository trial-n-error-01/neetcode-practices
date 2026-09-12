from collections import defaultdict


class Solution:

        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        masterlist=defaultdict(list)
        for str in strs:
            chars = [0]*26
            for char in str:
                chars[ord(char)-ord('a')]+=1
            masterlist[tuple(chars)].append(str)
        
        return list( masterlist.values())

