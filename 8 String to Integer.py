# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def myAtoi(self, string):
        """
        :type string: string
        :rtype: int
        """
        string = string.strip()
        if string:
            start = 0
            end = 0
            if string[0] == '-' or string[0] == '+':
                start += 1
                end += 1
            temp = [str(j) for j in range(10)]
            for i in range(start, len(string)):
                if string[i] in temp:
                    end += 1
                else:
                    break
            if start == end:
                return 0
            else:
                num = int(string[:end])
                if num < -2 ** 31:
                    return -2 ** 31
                elif num > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                else:
                    return num
        else:
            return 0


test = Solution()
print test.myAtoi('-123abcasdf')
