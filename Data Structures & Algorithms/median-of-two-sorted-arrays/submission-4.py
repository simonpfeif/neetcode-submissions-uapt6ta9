class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search on nums1
        # we know leftPartition = (n + m) // 2
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        half = (n + m) // 2 # target = leftPartitions
        l, r = 0, n - 1
        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2
            print("m2: ", m2)

            l1 = nums1[m1] if m1 >= 0 else float("-infinity")
            r1 = nums1[m1 + 1] if (m1 + 1) < n else float("infinity") 
            l2 = nums2[m2] if m2 >= 0 else float("-infinity")
            r2 = nums2[m2 + 1] if (m2 + 1) < m else float("infinity")

            if l1 <= r2 and l2 <= r1:
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                return min(r1, r2)
            elif l1 > r2:
                # make l1 smaller -> move r pointer
                r = m1 - 1
            else:
                # l2 > r1
                # make l1 bigger -> move l pointer
                l = m1 + 1
        return