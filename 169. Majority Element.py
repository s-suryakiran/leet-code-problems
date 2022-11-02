class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        def majority(i, j): 
            if i == j:
                return nums[i]
            
            mid = (j-i)//2 + i
            left = majority(i, mid)
            right = majority(mid+1, j)
            
            if left == right:
                return left
            
            leftc = sum(1 for k in range(i,j+1) if nums[k] == left)
            rightc = sum(1 for k in range(i,j+1) if nums[k] == right)
            
            if leftc > rightc:
                return left
            else:
                return right
        
        return majority(0, len(nums) -1)
        