class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            q = deque()
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            visited.add((row,col))
            q.append((row,col))

            while q:
                row, col = q.popleft()
                for direction in directions:
                    r = row + direction[0]
                    c = col + direction[1]
                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == "1" and ((r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)
        
        return islands

