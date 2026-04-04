class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = [0] * n

        for u, v in trust:
            delta[u - 1] -= 1
            delta[v - 1] += 1
            
        for i in range(n):
            if delta[i] == n - 1:
                return i + 1
        
        return -1