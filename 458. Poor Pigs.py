class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tmp = log2(buckets)
        minutesToTest = ceil(minutesToTest/minutesToDie)
        if minutesToTest == 1: 
            return ceil(tmp) 
        return ceil(tmp / log2(minutesToTest+1))