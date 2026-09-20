class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
             return ""
    
        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Check this character against all other strings
            for j in range(1, len(strs)):
                # If we reach the end of any string or find a mismatch
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                    
        return strs[0]