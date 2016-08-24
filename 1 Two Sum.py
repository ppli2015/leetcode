# -*-coding:cp936-*-
__author__ = 'lpp'

# 使用哈希表
# 避免同一个数字 3+3=6
# 可以扫描一次就完成

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (target - nums[i]) in nums and nums.index(target - nums[i]) != i:
                return [i, nums.index(target - nums[i])]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        for i in range(len(nums)):
            ht[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if ht.has_key(comp) and ht[comp] != i:
                return [i, ht[comp]]

    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if ht.has_key(comp):
                return [ht[comp], i]
            ht[nums[i]] = i


nums = [3, 2, 4]
target = 6
test = Solution()
indices = test.twoSum3(nums, target)
print indices
