"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        start = [i.start for i in intervals]
        start.sort()
        end = [i.end for i in intervals]
        end.sort()
        maxCount = 0
        c = 0
        i , j = 0, 0
        while i < len(intervals) and j < len(intervals):
            if start[i] < end[j]:
                c += 1
                i += 1
            else:
                c -= 1
                j += 1
            maxCount = max(c, maxCount)
        return maxCount

