class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        
        hashMap = {}

        for index in range(len(s)):
            hashMap[s[index]]=hashMap.get(s[index],0)+ 1
            hashMap[t[index]]=hashMap.get(t[index],0)-1
        
        print(hashMap)
        for index in hashMap:

            if(hashMap[index]!=0):
                return False
        
        return True