class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Use 9 integers to represent the digits seen in each row, col, and box.
        # We will use bits to track if a number (1-9) has been seen.
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                    
                # Convert string "1"-"9" to a bit position (0-8)
                bit = 1 << (int(val) - 1)
                
                # Calculate which 3x3 box we are in (0-8)
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Use bitwise AND to check if we've seen this bit before
                if (rows[r] & bit) or (cols[c] & bit) or (boxes[box_idx] & bit):
                    return False
                    
                # Use bitwise OR to register that we have now seen this number
                rows[r] |= bit
                cols[c] |= bit
                boxes[box_idx] |= bit
                
        return True