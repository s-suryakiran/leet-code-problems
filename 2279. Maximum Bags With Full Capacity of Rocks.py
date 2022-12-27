class Solution:
    def maximumBags(self, cap: List[int], rocks: List[int], more: int) -> int:
        for i in range(len(cap)):
            cap[i] -= rocks[i]
        i = 0
        cap.sort()
        
        while i < len(cap) and more - cap[i] >= 0:
            more -= cap[i]
            i += 1
        return i