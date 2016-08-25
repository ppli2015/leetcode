# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        count = len(s) - 1
        for i in range(len(s)):
            r += (ord(s[i]) - 64) * (26 ** count)
            count -= 1
        return r


test = Solution()
r = test.titleToNumber("")
print r
