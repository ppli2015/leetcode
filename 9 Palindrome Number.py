# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        print x
        for i in range(len(x) / 2):
            if x[i] != x[0 - i - 1]:
                return False
        return True


test = Solution()
print test.isPalindrome(0)
