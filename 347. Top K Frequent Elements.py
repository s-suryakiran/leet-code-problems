class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        d_sorted = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse= True)}
        i = 0
        ans = []
        for key,value in d_sorted.items():
            if i < k:
                ans.append(key)
            else:
                break
            i += 1
        return ans