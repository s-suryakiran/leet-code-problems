class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                neighbors[pattern].append(word)

        visited = set()
        res = 1
        q = deque()
        visited.add(beginWord)
        q.append(beginWord)
         
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
                
            res += 1
        return 0
