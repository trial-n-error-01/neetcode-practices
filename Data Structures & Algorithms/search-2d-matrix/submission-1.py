class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Previous was m Log(n)
        # This is log(mn)
        ROWS, COLS = len(matrix), len(matrix[0])

        l , r = 0, ROWS*COLS -1

        while(l<=r):
            m = l + (r-l)//2
            row, col = m//COLS, m% COLS
            if(target== matrix[row][col]):
                return True
            elif(target>matrix[row][col]):
                l= m + 1
            else:
                r=m-1

        return False         