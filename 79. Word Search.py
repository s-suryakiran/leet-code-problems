class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if r < 0 or c < 0 or r==ROWS or c==COLUMNS or i >= len(word) or board[r][c] != word[i] or (r,c) in visited:
                return False
            
            visited.add((r,c))

            if i==len(word)-1: 
                return True

            res =  dfs(r, c+1, i+1) or dfs(r, c-1, i+1) or dfs(r+1, c, i+1) or dfs(r-1, c, i+1)
            visited.remove((r,c))
            return res

            
        for r in range(ROWS):
            for c in range(COLUMNS):
                ans = dfs(r, c, 0)
                if ans:
                    return True
        return False