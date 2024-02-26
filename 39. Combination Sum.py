class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        def helper(i, comb, total):
            if total == target:
                combinations.append(comb.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            comb.append(candidates[i])
            helper(i, comb, total + candidates[i])
            comb.pop()
            helper(i+1, comb, total)

        helper(0, [], 0)
        return combinations