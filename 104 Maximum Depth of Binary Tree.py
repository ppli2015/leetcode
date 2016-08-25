# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        elif root.left == None:
            if root.right == None:
                return 1
            else:
                return 1 + self.maxDepth(root.right)
        else:
            if root.right == None:
                return 1 + self.maxDepth(root.left)
            else:
                return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


test = Solution()
r = test.maxDepth()
print r
