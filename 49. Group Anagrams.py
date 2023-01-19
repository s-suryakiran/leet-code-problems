class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        from collections import Counter
        for s in strs:
            count = [0] *26
            for c in s:
                count[ord(c)-ord("a")] += 1
    
            if d.get(tuple(count),"") =="":
                d[tuple(count)] = [s]
            else:
                d[tuple(count)].append(s)
        return d.values()
