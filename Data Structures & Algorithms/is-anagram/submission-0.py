class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        
        hashMap = {}
        for i in range(len(s)):
            hashMap[s[i]]= hashMap.get(s[i],0)+1
            hashMap[t[i]]= hashMap.get(t[i],0)-1

        for i in hashMap.values():
            if(i!=0):
                return False
        
        return True

