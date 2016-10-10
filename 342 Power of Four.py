# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num % 4 == 0:
            while num / 4 != 0 and num % 4 == 0:
                num /= 4
            if num == 1:
                return True
            else:
                return False
        else:
            if num == 1:
                return True
            else:
                return False


test = Solution()
print test.isPowerOfFour(1)
