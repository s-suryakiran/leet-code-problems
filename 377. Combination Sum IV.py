class Solution:
    def search(self,nums,target):
            if target < 0:
                return 0
            if target in self.dp:
                return self.dp[target]
            comb_sum = 0
            for num in nums:
                if target > num:
                    comb_sum = comb_sum + self.search(nums,target - num)
                elif target == num:
                    comb_sum = comb_sum + 1
            self.dp[target] = comb_sum
            return comb_sum
        
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.dp = {}
        self.dp[0] = [1]
        return self.search(nums,target)