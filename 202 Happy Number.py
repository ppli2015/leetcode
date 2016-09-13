#-*-coding:cp936-*-
__author__ = 'lpp'

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        templist = []
        l = [int(i)**2 for i in str(n)]
        s = sum(l)
        while s!=1:
            print s
            if templist.count(s)>0:
                return False
            templist.append(s)
            l = [int(i)**2 for i in str(s)]
            s = sum(l)
        return True

test = Solution()
print test.isHappy(19)