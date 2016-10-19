# -*-coding:cp936-*-
__author__ = 'lpp'


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n)==0:
            return n
        left = 1
        right = n
        temp = (left + right) / 2
        r = guess(temp)
        while r != 0:
            if r == 1:
                left = temp
                temp = (left + right) / 2
                r = guess(temp)
            else:
                right = temp
                temp = (left + right) / 2
                r = guess(temp)
        return temp
