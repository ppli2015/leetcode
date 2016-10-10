# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        else:
            dp = [nums[0], max(nums[0], nums[1])]
            for i in range(2, n):
                dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
            return dp[-1]

### dynamic programming
test = Solution()
print test.rob([1, 2, 2, 1, 2])
