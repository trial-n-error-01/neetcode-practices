class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Stack or Recursion is O(n) and O(n)

        # stack one
        stack = []
        
        for c in tokens:
            match c:
                case "+":
                    stack.append(stack.pop()+stack.pop())
                case "-":
                    operand1, operand2  = stack.pop(), stack.pop()
                    stack.append(operand2-operand1)
                case "*":
                    stack.append(stack.pop()*stack.pop())
                case "/":
                    
                    operand1, operand2  = stack.pop(), stack.pop()

                    stack.append(int(float(operand2)/operand1))
                case _:
                    stack.append(int(c))
        
        return(stack[0])
