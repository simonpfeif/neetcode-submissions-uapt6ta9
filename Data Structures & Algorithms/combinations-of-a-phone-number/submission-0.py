class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = []

        letter_hash = { 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        # i is digit iterator
        def dfs(i):
            if i >= len(digits):
                if curr:
                    res.append(''.join(curr))
                return
            
            for letter in letter_hash[int(digits[i])]:        
                curr.append(letter)
                dfs(i + 1)
                curr.pop()
        dfs(0)
        return res