# -*-coding:cp936-*-
__author__ = 'lpp'

# 滑动窗口
# 出现重复字符时，从第一次出现之后截断作为新的保留字符串
# 跳出循环，再确认一遍保留字符串

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = ''
        result = ''
        for c in s:
            if temp.find(c) == -1:
                temp += c
            else:
                if len(temp) > len(result):
                    result = temp
                temp = temp[temp.index(c) + 1:] + c
        if len(temp) > len(result):
            result = temp
        return len(result)


s = 'abcad'
test = Solution()
result = test.lengthOfLongestSubstring(s)
print result
