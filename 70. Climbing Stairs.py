class Solution:
    def climbStairs(self, n: int) -> int:
        m ={}
        m[1] = 1
        m[2] = 2
        
        def climb(n):
            if n in m: 
                return m[n]
            else:
                m[n] =  climb(n-1) + climb(n-2)
                return m[n]
        return climb(n)