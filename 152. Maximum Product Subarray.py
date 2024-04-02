class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = max(nums)
        curMin, curMax = 1,1

        for n in nums:
            if n == 0:
                curMin, curMax = 1,1
                continue
            tmp = curMax * n
            curMax = max(tmp, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            maxprod = max(maxprod, curMax)
        
        return maxprod

        