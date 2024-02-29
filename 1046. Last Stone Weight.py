class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-1*s for s in stones]
        heapq.heapify(maxheap)
        while(len(maxheap)>1):
            first = -1 * heapq.heappop(maxheap)
            second = -1 * heapq.heappop(maxheap)
            heapq.heappush(maxheap, -1 * (first - second))

        maxheap.append(0)
        return -1 * maxheap[0]
        