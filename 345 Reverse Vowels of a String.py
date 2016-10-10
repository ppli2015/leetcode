# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if len(s) < 2:
        #     return s
        vowel = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        start = 0
        end = len(s) - 1
        while start <= end:
            while s[start].lower() not in vowel and start < end:
                start += 1
            while s[end].lower() not in vowel and end > start:
                end -= 1
            if start < end:
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                start += 1
                end -= 1
            else:
                break
        return ''.join(s)


test = Solution()
print test.reverseVowels('aA')
