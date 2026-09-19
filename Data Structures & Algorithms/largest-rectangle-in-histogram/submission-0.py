class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        maxArea = 0
        stack = []

        for index in range(length+1):
            while stack and (index == length or heights[stack[-1]]>= heights[index]):
                height = heights[stack.pop()]
                width = index if not stack else index-stack[-1]-1
                maxArea = max(maxArea, height*width)
            stack.append(index)

        return maxArea 