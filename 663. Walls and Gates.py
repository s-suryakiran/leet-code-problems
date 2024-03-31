class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        q = deque()
        visited = set()
        rows, cols = len(rooms), len(rooms[0])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        dist = 0
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        while q:
            r,c = q.popleft()
            for i in range(len(q)):
                for direction in directions:
                    row = r + direction[0]
                    col = c + direction[1]
                    if (row,col) in visited or row < 0 or row >= rows or col < 0 or col >= cols or rooms[row][col] == -1:
                        continue
                    
                    rooms[row][col] = dist
                    visited.add((row,col))
                    q.append((row,col))
            dist += 1
        return rooms