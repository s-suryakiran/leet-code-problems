class Solution:
    def isPalindrome(self, s: str) -> bool:
        ds1=""
        ds=''.join(filter(str.isalnum, s.lower()))
        # print(ds)
        for i in range(len(ds)-1, -1,-1):
            ds1 = ds1+ds[i]
        # print(ds1)
        
        if ds1 == ds:
            return True
        return False