# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            if not dic1.has_key(s[i]):
                if not dic2.has_key(t[i]):
                    dic1[s[i]] = t[i]
                    dic2[t[i]] = s[i]
                else:
                    return False
            else:

                if dic1[s[i]] != t[i]:
                    return False
        return True


test = Solution()
print test.isIsomorphic('ab', 'aa')
