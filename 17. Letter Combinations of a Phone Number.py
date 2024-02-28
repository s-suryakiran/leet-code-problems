class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []

        ans = []
        s = []
        
        numtoletter = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        def helper(i, curstr):
            if len(curstr)==len(digits):
                ans.append(curstr[:])
                return

            for c in numtoletter[digits[i]]:
                helper(i+1, curstr + c)

        helper(0,"")
        return ans
        