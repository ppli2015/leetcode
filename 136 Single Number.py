#-*-coding:cp936-*-
__author__ = 'lpp'

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ### use xor to calculate
        result = 0
        for num in nums:
            result^=num
        return result

