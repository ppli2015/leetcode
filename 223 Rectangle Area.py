# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left1 = max(A, E)
        left2 = max(B, F)
        right1 = min(C, G)
        right2 = min(D, H)
        print left1, left2
        print right1, right2
        if left1 >= right1 or left2 >= right2:
            return (C - A) * (D - B) + (G - E) * (H - F)
        else:
            overlap = (right1 - left1) * (right2 - left2)
            return (C - A) * (D - B) + (G - E) * (H - F) - overlap


test = Solution()
print test.computeArea(-2, -2, 2, 2, -3, -2, 2, 3)
