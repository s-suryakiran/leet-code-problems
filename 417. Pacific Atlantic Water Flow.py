class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows, cols = len(heights),len(heights[0])
        ans = []
        def dfs(r, c, visited, prev_height):
            if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prev_height or (r,c) in visited:
                return

            visited.add((r,c))
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for direction in directions:
                dfs(r+direction[0], c + direction[1], visited, heights[r][c])


        for r in range(rows):
            dfs(r, 0, pacific, 0)
            dfs(r, cols-1, atlantic, 0)
        
        for c in range(cols):
            dfs(0, c, pacific, 0)
            dfs(rows-1, c, atlantic, 0)
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    ans.append([r,c])
        
        return ans

