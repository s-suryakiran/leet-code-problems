class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = 0
        totalSum = sum(nums)
        
        for i,num in enumerate(nums):
            sumRight = totalSum - num - sumLeft
            
            if(sumRight == sumLeft):
                return i
            sumLeft = sumLeft + num
            
        return -1

        