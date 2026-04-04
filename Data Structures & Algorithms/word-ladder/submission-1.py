class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # create hash, map strings to words:
        # c*t, *at, ca* -> cat
        # b*t, *at, ba* -> bat
        # b*g, *ag, ba* -> bag
        graph = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                graph[pattern].append(word)
        

        visit = set([beginWord])
        res = 1
        q = deque([beginWord])
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]

                    for nei in graph[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)


            res += 1
        return 0