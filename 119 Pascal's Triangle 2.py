# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 1:
            return [1]
        a = [1]
        for i in range(1, rowIndex + 1):
            b = [1]
            for j in range(1, i):
                b.append(a[j] + a[j - 1])
            b.append(1)
            a = b
        return b


test = Solution()
print test.getRow(0)
