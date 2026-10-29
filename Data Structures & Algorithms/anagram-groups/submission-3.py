class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        res = []

        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                res[groups[key]].append(word)
            else:
                groups[key] = len(res)
                res.append([word])
        
        return res
