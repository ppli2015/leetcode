# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(set(nums)) != len(nums):
            for i in range(len(nums) - 1):
                if nums[i:].count(nums[i]) > 1:
                    print nums[i + 1:]
                    j = nums[i + 1:].index(nums[i]) + i + 1
                    if (j - i) <= k:
                        return True
        return False


test = Solution()
print test.containsNearbyDuplicate([], 0)
