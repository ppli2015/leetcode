# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        temp = n
        now = 0
        while temp - 9 * (10 ** (i)) * (i + 1) > 0:
            temp -= 9 * (10 ** (i)) * (i + 1)
            now += 9 * (10 ** (i))
            i += 1
            print i, temp
        target = now + temp / (i + 1)
        w = temp % (i + 1)
        if w == 0:
            return int(str(target)[-1])
        else:
            return int(str(target + 1)[w - 1])


test = Solution()
print test.findNthDigit(190)
