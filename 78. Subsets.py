class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        word = []
        def dfs(i):
            if i >= len(nums):
                subsets.append(word.copy())
                return

            word.append(nums[i])
            dfs(i+1)

            word.pop()
            dfs(i+1)
        dfs(0)
        return subsets