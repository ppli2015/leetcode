# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        count = nums.count(0)
        if count == len(nums):
            pass
        else:
            for i in range(count):
                nums.remove(0)
                nums.append(0)

l = [0, 1, 0, 3, 4]
test = Solution()
r = test.moveZeroes(l)
print r
