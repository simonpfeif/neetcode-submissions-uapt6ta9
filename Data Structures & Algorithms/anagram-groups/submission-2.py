class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count = [0] * 26 -> convert to a str. This would be our key
        anagrams = {} # counts str: list of strs

        for s in strs:
            cnts = [0] * 26
            for c in s:
                cnts[ord(c) - ord('a')] += 1
                
            key = tuple(cnts)
            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(s)
        
        return list(anagrams.values())