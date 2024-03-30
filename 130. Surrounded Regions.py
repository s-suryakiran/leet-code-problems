class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        

        def mark(r,c):
            if r < 0 or r >= rows or c < 0 or c>=cols or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for direction in directions:
                mark(r+direction[0], c+direction[1])
            
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                    mark(r,c)


        for r in range(rows):
            for c in range(cols): 
                if board[r][c] == "O":
                    board[r][c] = "X"
        

        for r in range(rows):
            for c in range(cols): 
                if board[r][c] == "T":
                    board[r][c] = "O"
        