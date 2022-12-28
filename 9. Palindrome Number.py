class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = x
        x1 = 0
        while i>0:
            x1 = (x1*10)+(i%10)
            i = i//10
        if x1 == x:
            return True
        else:
            return False