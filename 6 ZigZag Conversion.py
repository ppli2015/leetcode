# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        result = ''
        sum_num = 2 * (numRows - 1)
        length = len(s)
        for i in range(numRows):
            a = sum_num - 2 * i
            temp = i
            count = 0
            l = []
            while temp < length:
                if not l:
                    l.append(temp)
                elif l[-1] == temp:
                    pass
                else:
                    l.append(temp)
                if count % 2 == 0:
                    temp += a
                else:
                    temp += sum_num - a
                count += 1
            for j in l:
                result += s[j]
        return result


test = Solution()
print test.convert('A', 0)
