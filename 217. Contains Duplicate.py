class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for num in nums:
            dup[num] = dup.get(num,0)+1
            if dup[num] > 1:
                return True
            
        return False
        