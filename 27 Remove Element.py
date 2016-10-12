# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while nums.count(val) > 0:
            nums.remove(val)
        return len(nums)


test = Solution()
print test.removeElement([2, 3, 3, 2], 3)
