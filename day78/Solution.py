from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and nums2[j - 1] > nums1[i]:
                # Increase i
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # Decrease i
                imax = i - 1
            else:
                # i is perfect, we found the right partition
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_of_left)

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

S = Solution()

# Testcase 1:
print(S.findMedianSortedArrays([1, 3], [2]))
# Output: 2.0

# Testcase 2:
print(S.findMedianSortedArrays([1, 2], [3, 4]))
# Output: 2.5

# Testcase 3:
print(S.findMedianSortedArrays([0, 0], [0, 0]))
# Output: 0.0