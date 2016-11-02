# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': 1, ')': 2, '{': 3, '}': 4, '[': 5, ']': 6}
        q = []
        for i in range(len(s)):
            if not q:
                q.append(s[i])
            else:
                if dic[s[i]] == dic[q[-1]] + 1:
                    q.pop()
                else:
                    q.append(s[i])
        if q:
            return False
        else:
            return True


test = Solution()
print test.isValid('([])')
