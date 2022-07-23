class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
  
        res  = [0] * len(nums)
        enum = list(enumerate(nums)) 
        
        self.mergeSort(enum, 0, len(nums) - 1, res)
        return res
    
    def mergeSort(self, enum, start, end, res):
        if start >= end: return
        
        mid = start + (end - start) // 2
        self.mergeSort(enum, start, mid, res)
        self.mergeSort(enum, mid + 1, end, res)
        self.merge(enum, start, mid, end, res)
    
    def merge(self, enum, start, mid, end, res):
        p, q = start, mid + 1
        inversion_count = 0
        
        while p <= mid and q <= end:
            if enum[p][1] <= enum[q][1]:
                res[enum[p][0]] += inversion_count
                p += 1
            else:
                inversion_count += 1
                q += 1
        
        while p <= mid:
            # res[enum[p][0]] += inversion_count
            res[enum[p][0]] += end - mid
            p += 1
        
        enum[start:end+1] = sorted(enum[start:end+1], key=lambda e:e[1])