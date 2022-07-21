class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = prices[0]
        min = prices[0]
        diff = 0
        for ele in prices:
            
            if max < ele:
                max = ele
                
            if min > ele:
                min = ele
                max = ele
            
            if (max-min) > diff:
                diff = max - min
        
        return diff