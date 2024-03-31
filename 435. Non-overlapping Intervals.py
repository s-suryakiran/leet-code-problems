class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])

        ans = 0
        previousEnd = intervals[0][1]

        for s,e in intervals[1:]:
            if previousEnd <= s:
                previousEnd = e
            else:
                ans += 1
                previousEnd = min(previousEnd, e)
        return ans
