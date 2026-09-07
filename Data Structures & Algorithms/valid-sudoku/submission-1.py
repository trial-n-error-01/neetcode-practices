class Solution:
    def checkNums(self, nums: List[str]) -> bool:
        arr = [0] * 9
        for n in nums:
            if n != '.':
                n = int(n)
                if n > 0 and n < 10:
                    arr[n-1] += 1
        
        for n in arr:
            if n > 1:
                return False
        return True
    
    def checkRows(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.checkNums(row):
                return False
        return True
    
    def checkCols(self, board: List[List[str]]) -> bool:
        cols = [[0] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                cols[i][j] = board[j][i]
        return self.checkRows(cols)

    def checkSubs(self, board: List[List[str]]) -> bool:
        for i in range(0,9,3):
            for j in range(0,9,3):
                arr = []
                for ii in range(3):
                    for jj in range(3):
                        arr.append(board[i + ii][j + jj])
                if not self.checkNums(arr):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkSubs(board)