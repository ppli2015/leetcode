# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        else:
            result = [[1]]
            for i in range(1, numRows):
                row = [1]
                for j in range(1, i):
                    if j < i:
                        row.append(result[i - 1][j] + result[i - 1][j - 1])
                row.append(1)
                result.append(row)
            return result


test = Solution()
result = test.generate(5)
for i in result:
    print i
