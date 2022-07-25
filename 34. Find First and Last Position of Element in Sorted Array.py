class Solution:
    def start_search(self, nums: List[int], target: int):
        f = 0
        l = len(nums) - 1
        start = -1
        
        while (f <= l):
            mid = (f + l) // 2
        
            if nums[mid] == target:
                start = mid
                l = mid - 1
                
            elif nums[mid] < target:
                f = mid + 1
            else:
                l = mid - 1
        
        return start
    
    def end_search(self, nums: List[int], target: int):
        f = 0
        l = len(nums) - 1
        end = -1
        
        while (f <= l):
            mid = (f + l) // 2
        
            if nums[mid] == target:
                end = mid
                f = mid + 1
                
            elif nums[mid] < target:
                f = mid + 1
            else:
                l = mid - 1
        
        return end
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        
        start = self.start_search(nums, target)
        end = self.end_search(nums, target)
        return [start, end]
       
                