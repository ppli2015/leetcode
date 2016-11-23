# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        r = []
        count = 0
        while count < (len(s) - len(p) + 1):
            temp = set(s[count:count + len(p)])
            if set(p) == temp:
                r.append(count)
                temp = set(s[count + 1:count + 1 + len(p)])
                if count + len(p) < len(s) - 1 and s[count] != s[count + len(p)]:
                    count += 1
            count += 1
        return r


test = Solution()
print test.findAnagrams("abacbabc","abc")
