class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.par = list(range(n))
        self.components = n

    def find(self, node):
        if node != self.par[node]:
            self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        
        self.components -= 1
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        
        return True


    def get_num_components(self):
        return self.components

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.get_num_components()
