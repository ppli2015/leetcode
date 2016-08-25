# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomList = list(ransomNote)
        magazineList = list(magazine)
        for i in set(ransomList):
            if ransomList.count(i) <= magazineList.count(i):
                pass
            else:
                return False
        return True


test = Solution()
r = test.canConstruct('aa', 'aab')
print r
