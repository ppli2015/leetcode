class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = 1
        length = len(s)
        while count * k < length:
            if count % 2 is 0:
                pass
            else:
                start = (count - 1) * k
                end = count * k
                s = s[:start] + self.reverse(s[start:end]) + s[end:]
            count += 1
        if count % 2 is 0:
            pass
        else:
            start = (count - 1) * k
            end = length
            s = s[:start] + self.reverse(s[start:end]) + s[end:]
        return s

    def reverse(self, s):
        l = list(s)
        l.reverse()
        return ''.join(l)


test = Solution()
print test.reverseStr('abcdefghijklmn', 2)
