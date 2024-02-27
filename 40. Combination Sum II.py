class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        if target <= 0:
            return 

        def helper(comb, i, csum):
            if target == csum:
                combinations.append(comb[:])
                return

            if i>=len(candidates) or csum > target:
                return

            comb.append(candidates[i])
            helper(comb, i+1, csum+candidates[i])

            comb.pop()

            while(i<len(candidates)-1 and candidates[i]==candidates[i+1]):
                i += 1 
            helper(comb, i+1, csum)
        
        helper([],0,0)
        return combinations