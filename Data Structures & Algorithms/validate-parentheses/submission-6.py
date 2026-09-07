class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {')':'(', 
                '}':'{',
                ']':'['}
        top_element = '#'
        for char in s:
            if char in maps:
                if not stack or stack.pop() != maps[char]:
                    return False
            else:
                stack.append(char)
        
        
        return len(stack)==0