class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        min_heap = []
        total = 0
        res = 0

        for t in transactions:
            total += t
            res += 1
            if t < 0:
                heapq.heappush(min_heap, t)
            
            if total < 0:
                total -= heapq.heappop(min_heap)
                res -= 1
        
        return res

        # n = len(transactions)
        
        # def dfs(i, cur, cnt):
        #     if i == n:
        #         return cnt
            
            
        #     if transactions[i] > 0:
        #         return dfs(i + 1, cur + transactions[i], cnt + 1)
            
        #     if transactions[i] + cur < 0:
        #         return dfs(i + 1, cur, cnt)

        #     return max(dfs(i + 1, cur + transactions[i], cnt + 1), dfs(i + 1, cur, cnt))
        
        # return dfs(0, 0, 0)

                
# [3,-2,3,-2,1,-1]
# 0,3,1,4,2,3,2
# res = 6

# [3,-3,-1,-2]
# res = 3