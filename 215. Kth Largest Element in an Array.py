class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            maxHeap.append(-1 * num)
        heapq.heapify(maxHeap)
        while k > 0:
            k -= 1
            a = heapq.heappop(maxHeap)

        return a*-1

        