class Solution:
    def romanMap(self, r:str)-> int:
        r_to_n = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        return r_to_n[r]
    
    def romanToInt(self, s: str) -> int:
        prev = 0
        total = 0
        for i in range(len(s)-1,-1,-1):
            n = self.romanMap(s[i])
            if n<prev:
                total = total - n
            else:
                total = total + n
            prev = n
        return total
                