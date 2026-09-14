class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                val = int(board[r][c]) - 1
                mask = 1 << val
                square = ((r // 3) * 3) + (c // 3)
                if (
                    rows[r] & mask or
                    cols[c] & mask or
                    squares[square] & mask
                ):
                    return False
                rows[r] |= mask
                cols[c] |= mask
                squares[square] |= mask
        
        return True