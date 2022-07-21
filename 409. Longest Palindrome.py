class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        size = len(s)
        for i in s:
            count[i] = count.get(i,0) + 1
        
        palcount = 0
        
        for key,value in count.items():
            
            if(value % 2 == 0):
                palcount = palcount + value
            
            else:
                palcount = palcount + value - 1
        
        if (size - palcount) != 0:
            palcount = palcount + 1
            
        return palcount
            