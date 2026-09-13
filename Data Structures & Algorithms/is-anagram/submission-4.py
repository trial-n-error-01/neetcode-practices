class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        
        # Since the problem states that the strings consist only of lowercase English letters, you don't actually need a hash map. You can use a fixed-size list of 26 integers to track character counts. This avoids the overhead of dictionary hashing and lookups.
        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
        # Check if all counts are zero
        return all(c == 0 for c in count)