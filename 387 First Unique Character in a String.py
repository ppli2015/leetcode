# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(s)
        newl = []
        for i in l:
            if i not in newl:
                newl.append(i)

        for i in newl:
            if l.count(i) == 1:
                return l.index(i)
        return -1


s = 'a'
test = Solution()
r = test.firstUniqChar(s)
print r
