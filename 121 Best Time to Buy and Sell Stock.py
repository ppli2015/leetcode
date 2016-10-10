# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if len(prices) < 2:
            return result
        elif prices[0] < prices[1]:
            min_ = prices[0]
            max_ = prices[1]
            result = max_ - min_
        else:
            min_ = prices[1]
            max_ = prices[1]
        # print 0,result
        for i in range(1, len(prices) - 1):
            if prices[i] >= prices[i + 1]:
                if prices[i + 1] < min_:
                    min_ = prices[i + 1]
                    max_ = prices[i + 1]
                    # result = 0
            else:
                if prices[i + 1] > max_:
                    max_ = prices[i + 1]
            if (max_ - min_) > result:
                result = max_ - min_
                # print i, result
        return result


l2 = [7, 1, 5, 3, 6, 4]
l3 = [2, 1, 2, 1, 0, 1, 2]
test = Solution()
print test.maxProfit(l2)
