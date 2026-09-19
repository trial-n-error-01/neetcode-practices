class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Stack or Recursion is O(n) and O(n)
        characters = '+-/*'
        # recursion
        def operation():
            token = tokens.pop()
            nonlocal characters
            if token not in characters:
                return int(token)
            
            right = operation()
            left = operation()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            else:
                return int(left /right)
        
        return operation()

