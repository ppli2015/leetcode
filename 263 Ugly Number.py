# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        if num != 1:
            return False
        else:
            return True


test = Solution()
print test.isUgly(12)
