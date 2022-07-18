class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) == len(t)):
            sList= list(s)
            tList = list(t)
            d = dict(zip(sList,tList))
            
            if max((dict(Counter(d.values()))).values())>1:
                return False
            
            for index, element in enumerate(sList):
                sList[index]=d[element]
            if sList == tList:
                return True
            
        return False