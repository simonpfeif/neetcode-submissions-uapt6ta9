class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        l = 0
        cur_diff = 0
        cnt = 0

        for r in range(minutes):
            if grumpy[r]:
                cur_diff += customers[r]
            else:
                cnt += customers[r]
        max_diff =  cur_diff
        

        for r in range(minutes, n):
            if grumpy[l]:
                cur_diff -= customers[l]
            l += 1
                
            if grumpy[r]:
                cur_diff += customers[r]
            else:
                cnt += customers[r]
            
            max_diff = max(max_diff, cur_diff)
        
        return cnt + max_diff

# customers = [1,0,1,2,1,1,7,5]
# grumpy =    [0,1,0,1,0,1,0,1]
# result =.   [1,0,1,0,1,0,7,0]
# max_diff = 6
# cnt = 10
# minutes = 3