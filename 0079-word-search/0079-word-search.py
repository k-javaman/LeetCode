class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        
        def backtrack(c,r,i):
            if i == len(word):
                return True
            
            if c < 0 or r < 0 or c >= COLS or r >= ROWS or not board[r][c] == word[i] or (r,c) in path:
                return False
            
            path.add((r,c))
            res = (backtrack(c+1,r,i+1) or
                   backtrack(c-1,r,i+1) or
                   backtrack(c,r+1,i+1) or
                   backtrack(c,r-1,i+1))
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(c,r,0):
                    return True
        return False