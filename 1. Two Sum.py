class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(0,len(nums)):
            remaining = target - nums[i]
           
            if remaining in visited:
                return [i, visited[remaining]]
            
            visited[nums[i]] = i

        # for i in range(0,len(nums)):
        #     a = nums.copy()
        #     a.pop(i)
        #     diff = target - nums[i]
        #     if (diff in a):
        #         s = a.index(diff)
        #         if s >= i:
        #             return i, s+1
        #         else:
        #             return i, s
            
