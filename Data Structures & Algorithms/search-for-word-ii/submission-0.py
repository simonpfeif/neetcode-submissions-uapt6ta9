class TrieNode():
    def __init__(self):
        self.children = {}
        self.index = -1
    
    def insert(self, curr, word, i):
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.index = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # insert into trie
        root = TrieNode()
        for i, word in enumerate(words):
            root.insert(root, word, i)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, node):
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in visit or 
                board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            if node.index != -1:
                res.add(words[node.index])
                node.index = -1
            
            for d in directions:
                row, col = r + d[0], c + d[1]
                dfs(row, col, node)
            visit.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        return list(res)
                        

