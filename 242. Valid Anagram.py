class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict = {}
        for i in s:
            c = sDict.get(i, 0) + 1
            sDict[i] = c
        
        for i in t:
            if i not in sDict.keys():
                return False
            if sDict[i] == 0:
                return False
            
            sDict[i] = sDict[i] - 1
            
        return True
    