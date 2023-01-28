class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_c = 0
        for i in nums:
            c = 0
            if (i-1) not in nums_set:
                while i in nums_set:
                    c = c + 1
                    i = i + 1
                max_c = max(c,max_c)
        return max_c