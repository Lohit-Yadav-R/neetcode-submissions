class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visited = set()
        queue = deque()
        queue.append([beginWord, 1])
        visited.add(beginWord)
        while queue:
            curWord, pathLen = queue.popleft()
            print(curWord)
            if curWord == endWord:
                    return pathLen
            for word in wordList:
                if word in visited:
                    continue
                diff = 0
                for i in range(len(curWord)):
                    if curWord[i] != word[i]:
                        diff += 1
                if diff == 1:
                    queue.append([word, pathLen + 1])
                    visited.add(word)
        
        return 0