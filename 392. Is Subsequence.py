class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        sList = list(s)
        tList = list(t)
        
        while((i < len(s)) and (j < len(t))):
            if (sList[i] == tList[j]):
                i = i + 1
                j = j + 1
                
            else:
                j = j + 1
                
        if (i == len(s)):
            return True
        
        return False
            
            
        