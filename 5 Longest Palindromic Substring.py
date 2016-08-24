# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        length = len(s)
        for i in range(length * 2 - 1):
            if i % 2 == 0:
                c = i / 2
                j = 1
                while (c - j) >= 0 and (c + j) < length:
                    if s[c - j] == s[c + j]:
                        j += 1
                    else:
                        break
                j = j - 1
                temp = s[c - j:c + j + 1]
                # print c,temp
                if len(result) < len(temp):
                    result = temp
            else:
                c1 = (i - 1) / 2
                c2 = (i + 1) / 2
                j = 0
                while (c1 - j) >= 0 and (c2 + j) < length:
                    if s[c1 - j] == s[c2 + j]:
                        j += 1
                    else:
                        break
                if j > 0:
                    j = j - 1
                    temp = s[c1 - j:c2 + j + 1]
                    # print c1,temp
                    if len(result) < len(temp):
                        result = temp
        return result

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Manacher's Algorithm
        # time complexity O(n)
        # space complexity O(n)
        ss = '/'
        for i in range(len(s)):
            ss += '#'
            ss += s[i]
        ss += '#\\'
        p = [0] * len(ss)
        mx = 0
        id = 0
        for i in range(len(ss) - 1):
            if mx > i:
                p[i] = min(p[2 * id - i], mx - i)
            else:
                p[i] = 1
            while ss[i + p[i]] == ss[i - p[i]]:
                p[i] += 1
            if (i + p[i]) > mx:
                mx = i + p[i]
                id = i
        index = p.index(max(p))
        return ss[index - p[index] + 1:index + p[index]].replace('#', '')


s = 'ababaccc'
test = Solution()
result = test.longestPalindrome2(s)
print result
