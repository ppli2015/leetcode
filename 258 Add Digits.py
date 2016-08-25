# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = sum(map(int, str(num)))
        return num


test = Solution()
result = test.addDigits(78)
print result
