# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        x = 0
        while 2 ** x <= n:
            x += 1
        x -= 1
        for i in range(x, -1, -1):
            if 2 ** i <= n:
                count += 1
                n -= 2 ** i
        return count


test = Solution()
count = test.hammingWeight(16)
print count
