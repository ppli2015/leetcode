# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            sl = list(s)
            tl = list(t)
            for i in set(sl):
                if sl.count(i) == tl.count(i):
                    pass
                else:
                    return False
            return True
        else:
            return False


test = Solution()
r = test.isAnagram('', '')
print r
