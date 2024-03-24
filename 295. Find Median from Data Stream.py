class MedianFinder:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
    
# class MedianFinder:
#     def __init__(self):
#         self.minHeap, self.maxHeap = [], []
        
#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.maxHeap, -num)
#         heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

#         if len(self.minHeap) > len(self.maxHeap):
#             heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        

#     def findMedian(self) -> float:

#         if len(self.minHeap) == len(self.maxHeap):
#             return (-self.maxHeap[0] + self.minHeap[0])/2

#         else:
#             return -self.maxHeap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
        
