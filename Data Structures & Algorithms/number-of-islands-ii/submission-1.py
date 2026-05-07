class UnionFind:
    def __init__(self, size):
        self.count = 0
        self.rank = [1] * size
        self.par = [-1] * size
    
    def add_land(self, n):
        if self.is_land(n):
            return
        self.par[n] = n
        self.count += 1
    
    def is_land(self, n):
        return self.par[n] >= 0
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            # already unioned
            return

        self.count -= 1

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:            
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)
        res = []

        for r, c in positions:
            uf.add_land(r * n + c)

            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and uf.is_land(nr * n + nc):
                    uf.union(r * n + c, nr * n + nc)
            
            res.append(uf.count)

        return res