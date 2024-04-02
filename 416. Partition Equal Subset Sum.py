class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total//2
        if total % 2 != 0:
            return False
        
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            tempdp = set()
            t = nums[i]
            for d in dp:
                if d+t == target:
                    return True
                tempdp.add(d)
                tempdp.add(d+t)
            dp = tempdp
        return False
