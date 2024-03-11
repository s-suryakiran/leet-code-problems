class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countDict = Counter(tasks)
        maxHeap = [-1*i for i in countDict.values()]
        heapq.heapify(maxHeap)
        totalTime = 0
        q = deque()
        while(maxHeap or q):
            totalTime += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt,totalTime+n])

            if q and q[0][1]==totalTime:
                heapq.heappush(maxHeap, q[0][0])
                q.popleft()
        return totalTime
        