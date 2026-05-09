class UnionFind:
    def __init__(self, size):
        self.count = 0
        self.par = [-1] * size
        self.rank = [1] * size
    
    def is_land(self, n):
        return self.par[n] >= 0
    
    def add_land(self, n):
        if self.is_land(n):
            return
        self.par[n] = n
        self.count += 1
    
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
            pos = r * n + c

            if uf.is_land(pos):
                res.append(uf.count)
                continue
            
            uf.add_land(pos)

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = r + dr, c + dc
                new_pos = nr * n + nc
                if nr >= 0 and nc >= 0 and nr < m and nc < n and uf.is_land(new_pos):
                    uf.union(pos, new_pos)
            
            res.append(uf.count)
        
        return res