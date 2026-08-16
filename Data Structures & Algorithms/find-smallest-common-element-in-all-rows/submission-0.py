class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for cur in mat[0]:
            found = True
            for row in mat[1:]:
                if not self.binarySearch(cur, row):
                    found = False
                    break
            if found: 
                return cur
        
        return -1


    def binarySearch(self, target, row):
        l, r = 0, len(row) - 1
        # print(target, row)
        
        while l <= r:
            m = (l + r) // 2
            # print(m)

            if row[m] == target:
                # print("res: True")
                return True
            elif row[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        # print("res: False")
        return False



# binary search on everything: 
# Time: m * log(n)
# Memory: O(1)

# Store each in a set
# Time: m * n
# Memory: O(m * n)