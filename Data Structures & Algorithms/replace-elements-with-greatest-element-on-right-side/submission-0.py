class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        cur = arr[n - 1]
        arr[n - 1] = -1
        for i in range(n - 2, -1, -1):
            nxt = max(arr[i], cur)
            arr[i] = cur
            cur = nxt
        
        return arr

