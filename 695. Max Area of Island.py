class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            q = deque()
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            visited.add((row,col))
            q.append((row,col))
            area = grid[row][col]
            while q:
                row, col = q.popleft()
                for direction in directions:
                    r = row + direction[0]
                    c = col + direction[1]
                    if (r in range(rows)) and (c in range(cols)) and (grid[r][c] == 1) and ((r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
                        area += 1
            return area

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    area = bfs(r, c)
                    maxArea = max(area, maxArea)

        return maxArea


#dfs:

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         visit = set()

#         def dfs(r, c):
#             if (
#                 r < 0
#                 or r == ROWS
#                 or c < 0
#                 or c == COLS
#                 or grid[r][c] == 0
#                 or (r, c) in visit
#             ):
#                 return 0
#             visit.add((r, c))
#             return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

#         area = 0
#         for r in range(ROWS):
#             for c in range(COLS):
#                 area = max(area, dfs(r, c))
#         return area