class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    # find the parent given a node
    def find(self, node):
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return node
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += 1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} # email -> index of account

        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        emailGroup = defaultdict(list) # index of acc -> list of emails
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for accIndex, emails in emailGroup.items():
            name = accounts[accIndex][0]
            res.append([name] + sorted(emails))
        return res

        
        
        
        
        
        
        
        