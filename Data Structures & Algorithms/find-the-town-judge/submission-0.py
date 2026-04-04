class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = {}
        
        for u, v in trust:
            if u not in people:
                people[u] = set()
            people[u].add(v)

        for person in range(1, n + 1):
            if person not in people:
                res = True
                for nei in range(1, n + 1):
                    if nei == person:
                        continue
                    if nei not in people:
                        return -1
                    if person not in people[nei]:
                        res = False
                        break
                
                if res:
                    return person
        return -1