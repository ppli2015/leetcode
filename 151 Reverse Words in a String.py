class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        start = 0
        end = len(words) - 1
        while start < end:
            temp = words[start]
            words[start] = words[end]
            start += 1
            words[end] = temp
            end -= 1
        return ' '.join(words)

    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        return ' '.join(words)


test = Solution()
print test.reverseWords2("the sky is blue")
