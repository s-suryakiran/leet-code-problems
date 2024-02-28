class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        colset = set()
        posdiagonalset = set()
        negdiagonalset = set()
        chessboard = [["."] * n for _ in range(n)]

        def helper(r):
            if r == n:
                ans.append(["".join(chessboard[i]) for i in range(n)])
                return
            
            for c in range(n):
                if c in colset or r+c in posdiagonalset or r-c in negdiagonalset:
                    continue
                
                colset.add(c)
                posdiagonalset.add(r+c)
                negdiagonalset.add(r-c)
                chessboard[r][c] = "Q"
                helper(r+1)

                colset.remove(c)
                posdiagonalset.remove(r+c)
                negdiagonalset.remove(r-c)
                chessboard[r][c] = "."
        helper(0)
        return ans
        