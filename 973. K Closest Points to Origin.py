class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for [x,y] in points:
            dist = x**2 + y**2
            minHeap.append([dist,x,y])
        heapq.heapify(minHeap)

        while k > 0:
            k -= 1
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        return res