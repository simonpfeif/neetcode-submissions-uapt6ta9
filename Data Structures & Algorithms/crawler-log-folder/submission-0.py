class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for op in logs:
            if op == "../":
                res = max(0, res - 1)
            elif op == "./":
                continue
            else:
                res += 1
        
        return res