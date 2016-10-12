# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        n = max(len(num1), len(num2))
        count = 0
        l = []
        for i in range(n):
            if i < len(num1) and i < len(num2):
                sum = int(num1[i]) + int(num2[i]) + count
            elif i < len(num1):
                sum = int(num1[i]) + count
            elif i < len(num2):
                sum = int(num2[i]) + count
            l.append(str(sum % 10))
            count = sum / 10
        if count > 0:
            l.append(str(count))
        print ''.join(l[::-1])


test = Solution()
print test.addStrings('123', '8989')
