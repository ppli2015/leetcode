# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        limit = int(len(nums) / 2.0)
        for i in set(nums):
            if nums.count(i) > limit:
                return i


test = Solution()
r = test.majorityElement([1,1,1,2,2,2,1])
print r
