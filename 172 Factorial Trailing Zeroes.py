# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # li = [i for i in range(1,n+1)]
        # print li

        count5 = n / 5
        result = n / 5
        while count5 > 0:
            count5 = count5 / 5
            result += count5
        return result


test = Solution()
num = 40000
print test.trailingZeroes(num)

count = 1
for i in range(1, num + 1):
    count *= i
r = 0
for i in str(count)[::-1]:
    if i == '0':
        r += 1
    else:
        break
print r
