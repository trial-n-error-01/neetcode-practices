class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()

        while n not in visited:
            visited.add(n)

            output = 0

            while n:
                digit = n%10
                digit **= 2
                output += digit
                n //=10

            if output == 1:
                return True
            else:
                n = output
        return False

        