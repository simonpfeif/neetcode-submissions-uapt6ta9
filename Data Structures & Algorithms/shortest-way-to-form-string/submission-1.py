class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        source_chars = set(source)
        for c in target:
            if c not in source_chars:
                return -1

        source_i = 0
        m = len(source)
        res = 0

        for c in target:
            if source_i == 0:
                res += 1

            while source[source_i] != c:
                source_i = (source_i + 1) % m

                if source_i == 0:
                    res += 1

            source_i = (source_i + 1) % m
        return res