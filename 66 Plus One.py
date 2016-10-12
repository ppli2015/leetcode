# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        jinwei = (digits[-1] + 1) / 10
        digits[-1] = (digits[-1] + 1) % 10
        for i in range(len(digits) - 2, -1, -1):
            temp = (digits[i] + jinwei) % 10
            jinwei = (digits[i] + jinwei) / 10
            digits[i] = temp
            print i
        if jinwei > 0:
            digits = [jinwei] + digits
        return digits


test = Solution()
print test.plusOne([9, 9, 9, 9, 9])
