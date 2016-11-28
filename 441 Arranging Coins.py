# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        all = 0
        i = 0
        while all <= n:
            all += i + 1
            i += 1
        return i-1


test = Solution()
print test.arrangeCoins(15)
