# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        dic = {}
        dic2 = {}
        for i in range(len(pattern)):
            p = pattern[i]
            if dic.has_key(p):
                if dic[p] != words[i]:
                    return False
            else:
                dic[p] = words[i]
                if dic2.has_key(words[i]):
                    return False
                else:
                    dic2[words[i]] = p
        return True


test = Solution()
print test.wordPattern('abba', "a a a a")
