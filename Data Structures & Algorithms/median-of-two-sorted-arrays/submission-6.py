class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half_len = (m + n) // 2
        l, r = 0, m - 1

        while True:
            i = (l + r) // 2
            j = half_len - i - 2
            

            Aleft = nums1[i] if i >= 0 else float('-infinity')
            Aright = nums1[i + 1] if (i + 1) < m else float('infinity')
            Bleft = nums2[j] if j >= 0 else float('-infinity')
            Bright = nums2[j + 1] if (j + 1) < n else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Bleft > Aright:
                # need to make A bigger
                l = i + 1
            else:
                r = i - 1
        