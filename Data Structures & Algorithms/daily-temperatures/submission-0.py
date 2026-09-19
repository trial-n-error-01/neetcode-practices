class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack implementation
        res = [0]*len(temperatures)

        stack = []

        for index, tempValue in enumerate(temperatures):
            # print(index)
            # print(stack)
            # print(res)

            while stack and tempValue > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            

            stack.append((tempValue, index))
        
        return res