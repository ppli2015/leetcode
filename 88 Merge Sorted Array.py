# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n < 1:
            return
        elif m < 1:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        i = 0
        j = 0
        while j < n:
            if nums1[i] <= nums2[j] and i < m + j:
                i += 1
            else:
                for temp in range(m + j, i, -1):
                    nums1[temp] = nums1[temp - 1]
                nums1[i] = nums2[j]
                i += 1
                j += 1


test = Solution()
test.merge([2, 0, 0], 1, [1, 3], 2)
