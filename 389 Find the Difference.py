#-*-coding:cp936-*-
__author__ = 'lpp'

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_ = list(s)
        t_ = list(t)
        for x in t_:
            if s.find(x)!=-1 and s_.count(x)==t_.count(x):
                pass
            else:
                return x

