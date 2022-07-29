class Solution:
    from collections import Counter
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        finalList = [] 
        for word in words:
            if(len(word) == len(pattern)):
                d = {}
                s = ""
                for i in range(0,len(word)):
                    if word[i] not in d.values():
                        d[pattern[i]] = d.get(pattern[i],word[i])
                    s = s + d.get(pattern[i],"0")   
                if s == word:
                    finalList.append(word)
        return finalList