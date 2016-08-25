# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 4:
            return self.canWinNim(n - 1) or self.canWinNim(n - 2) or self.canWinNim(n - 3)
        elif n < 4:
            return True
        else:
            return False

    def canWinNim2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0


test = Solution()
for i in range(1000):
    if not test.canWinNim2(i):
        print i
        # result = test.canWinNim()
        # print result
