# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return self.toHex(num + 16 ** 8)
        elif num == 0:
            return '0'
        else:
            r = []
            while num / 16 != 0:
                yu = num % 16
                if yu > 9:
                    yu = chr(yu + 87)
                r.append(str(yu))
                num /= 16
            if num > 0:
                if num > 9:
                    num = chr(num + 87)
                r.append(str(num))
            return ''.join(r[::-1])


test = Solution()
print test.toHex(-2)
