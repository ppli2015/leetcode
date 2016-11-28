# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    ### regard p as a sliding window on s, use dict to count items in the window.
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(p)):
            if dict1.has_key(p[i]):
                dict1[p[i]] += 1
            else:
                dict1[p[i]] = 1
        dict2 = {}
        if len(s) < len(p):
            return []
        else:
            r = []
            for i in range(len(p)):
                if dict2.has_key(s[i]):
                    dict2[s[i]] += 1
                else:
                    dict2[s[i]] = 1
            if dict1 == dict2:
                r.append(0)
            for i in range(0, len(s) - len(p)):
                dict2[s[i]] -= 1
                if dict2[s[i]] == 0:
                    del dict2[s[i]]
                new_one = s[i + len(p)]
                if dict2.has_key(new_one):
                    dict2[new_one] += 1
                else:
                    dict2[new_one] = 1
                if dict2 == dict1:
                    r.append(i + 1)
        return r


test = Solution()
print test.findAnagrams("cbaebabacd", "abc")
