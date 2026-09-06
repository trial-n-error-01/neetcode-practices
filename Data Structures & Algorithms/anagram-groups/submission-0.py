from collections import defaultdict


class Solution:

        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups=defaultdict(list)
        for n in strs:
            charSet =[0]*26

            for k in n:
                charSet[ord(k)-ord('a')]+=1;
            
            groups[tuple(charSet)].append(n)
        return list(groups.values())