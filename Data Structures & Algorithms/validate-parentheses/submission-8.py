class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapsForCloseToOpen = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        for character in s:

            if (character not in mapsForCloseToOpen):
                stack.append(character)
            else:
                if( stack and stack[-1]==mapsForCloseToOpen[character]):
                    stack.pop()
                else:
                    return False
        return True if not stack else False