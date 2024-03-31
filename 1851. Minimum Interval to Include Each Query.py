class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minHeap = []
        ans, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]) )
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            ans[q] = minHeap[0][0] if minHeap else -1

        return [ans[q] for q in queries]
