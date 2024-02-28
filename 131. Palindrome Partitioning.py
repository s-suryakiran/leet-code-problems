class Solution:
    def isPalindrome(self,s,i,j):
        while i < j:
            if s[i]!=s[j]:
                return False
            i,j = i+1, j-1
        return True
            
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        partition = []

        def helper(i):
            if i>=len(s):
                ans.append(partition[:])
                return
            
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    partition.append(s[i:j+1])
                    helper(j+1)
                    partition.pop()
        helper(0)
        return ans
