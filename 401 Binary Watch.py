# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 8:
            return []
        else:
            ans = []
            for i in range(1024):
                if bin(i).count('1') == num:
                    # >> 6 二进制右移六位，& 0x3f 二进制后六位，0x3f表示111111
                    h, m = i >> 6, i & 0x3f
                    if h < 12 and m < 60:
                        ans.append('%d:%02d' % (h, m))
            return ans


test = Solution()
print test.readBinaryWatch(0)
