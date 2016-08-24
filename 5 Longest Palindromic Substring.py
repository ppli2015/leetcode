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
        


s = 'ababacccccc'
test = Solution()
result = test.longestPalindrome(s)
print result
