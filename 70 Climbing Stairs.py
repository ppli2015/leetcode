# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 1]
        for i in range(2, n + 1):
            res.append(res[-1] + res[-2])
        return res[-1]


n = 35
test = Solution()

# print test.climbStairs(n)
print test.climbStairs2(n)
