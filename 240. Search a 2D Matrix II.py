class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = len(matrix[0])
        b = len(matrix)
        x = 0
        y = b - 1
        while (x < l) and (y >=0):
            if (target == matrix[y][x]):
                return True
            elif (target < matrix[y][x]):
                y = y - 1
            else:
                x = x + 1
                
                
        return False

        