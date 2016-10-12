# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        if count > 1:
            n = 1
            while n < count:
                if nums[n] == nums[n - 1]:
                    nums.remove(nums[n])
                    count -= 1
                else:
                    n += 1
        return len(nums)

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        if count > 0:
            i = 0
            for j in range(1, count):
                if nums[j] != nums[i]:
                    i += 1
                    nums[i] = nums[j]
            return i + 1
        else:
            return 0


test = Solution()
print test.removeDuplicates2([1, 1, 2])
