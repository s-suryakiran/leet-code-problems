class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        randict = {}
        
        for i in magazine:
            randict[i] = randict.get(i, 0)+1
        
        for i in ransomNote:
            if randict.get(i,0) > 0:
                randict[i] = randict[i] - 1
            else:
                return False
            
        return True