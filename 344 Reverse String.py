# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in range(len(s)):
            result += s[len(s) - 1 - i]
        return result

    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return ''.join(reversed(s))
        return s[::-1]

test = Solution()
r = test.reverseString2('abcde')
print r
