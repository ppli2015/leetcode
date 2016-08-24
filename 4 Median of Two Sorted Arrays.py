# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_sum = len(nums1) + len(nums2)
        count = 0
        if len_sum % 2 == 1:
            target = (len_sum - 1) / 2
            while nums1 and nums2:
                if count == target:
                    return float(min(nums1[0], nums2[0]))
                if nums1[0] < nums2[0]:
                    nums1.remove(nums1[0])
                else:
                    nums2.remove(nums2[0])
                count += 1
            if not nums1:
                while count != target:
                    nums2.remove(nums2[0])
                    count += 1
                return float(nums2[0])
            else:
                while count != target:
                    nums1.remove(nums1[0])
                    count += 1
                return float(nums1[0])

        else:
            target = len_sum / 2 - 1
            while nums1 and nums2:
                if count == target:
                    if nums1[0] < nums2[0] and len(nums1) > 1:
                        return (nums1[0] + min(nums1[1], nums2[0])) / 2.0
                    elif len(nums2) > 1:
                        return (nums2[0] + min(nums1[0], nums2[1])) / 2.0
                    else:
                        return (nums1[0] + nums2[0]) / 2.0
                if nums1[0] < nums2[0]:
                    nums1.remove(nums1[0])
                else:
                    nums2.remove(nums2[0])
                count += 1
            if not nums1:
                while count != target:
                    nums2.remove(nums2[0])
                    count += 1
                return (nums2[0] + nums2[1]) / 2.0
            else:
                while count != target:
                    nums1.remove(nums1[0])
                    count += 1
                return (nums1[0] + nums1[1]) / 2.0


nums1 = [1, 2]
nums2 = [3, 4]
test = Solution()
result = test.findMedianSortedArrays(nums1, nums2)
print result
