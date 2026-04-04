class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        while n != self.par[n]:
            # using path compression
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAcc = {}
        uf = UnionFind(len(accounts))

        for i, emails in enumerate(accounts):
            for e in emails[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list)
        for e, a in emailToAcc.items():
            leader = uf.find(a)
            emailGroup[leader].append(e)
        
        res = []
        for a, emails in emailGroup.items():
            name = accounts[a][0]
            res.append([name] + sorted(emails))
        
        return res
            
            
            
            
            
            
            
            
            
            
            
            
            