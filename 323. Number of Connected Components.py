class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        for n1,n2 in edges:
            n -= union(n1,n2)
        
        return n
