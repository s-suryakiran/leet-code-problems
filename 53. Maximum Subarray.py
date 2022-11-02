class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cmax = 0
        maxsum = -inf
        for i in nums:
            cmax = max(i, cmax+i)
            maxsum = max(maxsum, cmax)
        return maxsum
        