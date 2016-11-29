# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip():
            return len(s.split()[-1])
        else:
            return 0


test = Solution()
print test.lengthOfLastWord('1 2 34')
