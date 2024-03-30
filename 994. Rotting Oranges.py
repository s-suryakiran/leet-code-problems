class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                
                for direction in directions:
                    row, col = r+direction[0], c+direction[1]
                    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
                        continue
                        
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row,col))
            time += 1
        
        return time if fresh == 0 else -1
