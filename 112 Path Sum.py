# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            templist = [root]
            while templist[-1].left or templist[-1].right:
                if templist[-1].left:
                    templist.append(templist[-1].left)
                else:
                    templist.append(templist[-1].right)

            r = []
            for i in templist:
                r.append(i.val)
            if self.getSum(r) == sum:
                return True
            while len(templist) > 1:
                if templist[-1] == templist[-2].right:
                    templist.remove(templist[-1])
                else:
                    templist.remove(templist[-1])
                    if templist[-1].right:
                        templist.append(templist[-1].right)
                        while templist[-1].left or templist[-1].right:
                            if templist[-1].left:
                                templist.append(templist[-1].left)
                            else:
                                templist.append(templist[-1].right)
                        r = []
                        for i in templist:
                            r.append(i.val)
                        if self.getSum(r) == sum:
                            return True
            return False
        else:
            return False

    def getSum(self, l):
        return sum(l)


test = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = None
root.left.left.right = TreeNode(6)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(7)
print test.hasPathSum(root, 11)
