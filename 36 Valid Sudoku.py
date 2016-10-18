# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) == 9 and len(board[0]) == 9:
            if self.check(board):
                pass
            else:
                return False
            tempboard = []
            for i in range(9):
                list2 = []
                for j in range(9):
                    list2.append(board[j][i])
                tempboard.append(list2)
            if self.check(tempboard):
                pass
            else:
                return False

            tempboard = []
            for j in range(0, 7, 3):
                list1 = []
                list2 = []
                list3 = []
                for i in range(j, j + 3):
                    print i, j
                    list1 += board[i][0:3]
                    list2 += board[i][3:6]
                    list3 += board[i][6:9]
                tempboard.append(list1)
                tempboard.append(list2)
                tempboard.append(list3)
            if self.check(tempboard):
                pass
            else:
                return False
            return True
        else:
            return False

    def check(self, templist):
        for l in templist:
            if l.count('.') == 9 - len(set(list(l))) + 1:
                pass
            else:
                return False
        return True


