# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        r = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    pass
                else:
                    if row > 1:
                        if i == 0:
                            r += 1
                            if grid[i + 1][j] == 0:
                                r += 1
                        elif i == (row - 1):
                            r += 1
                            if grid[i - 1][j] == 0:
                                r += 1
                        else:
                            if grid[i + 1][j] == 0:
                                r += 1
                            if grid[i - 1][j] == 0:
                                r += 1
                    else:
                        r += 2
                    if col > 1:
                        if j == 0:
                            r += 1
                            if grid[i][j + 1] == 0:
                                r += 1
                        elif j == (col - 1):
                            r += 1
                            if grid[i][j - 1] == 0:
                                r += 1
                        else:
                            if grid[i][j + 1] == 0:
                                r += 1
                            if grid[i][j - 1] == 0:
                                r += 1
                    else:
                        r += 2
        return r


test = Solution()
print test.islandPerimeter([[1]])
