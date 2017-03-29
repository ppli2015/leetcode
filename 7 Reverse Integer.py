class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            flag = 1
            x = -x
        elif x == 0:
            return 0
        l = []
        while x != 0:
            l.append(x % 10)
            x /= 10
        result = int(''.join([str(i) for i in l]))
        if flag:
            if -result < -2 ** 31:
                return 0
            else:
                return -result
        else:
            if result > 2 ** 31 - 1:
                return 0
            else:
                return result


test = Solution()
print test.reverse(0)
