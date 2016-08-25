# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None:
            new_root = TreeNode(root.val)
            new_root.right = self.invertTree(root.left)
            new_root.left = self.invertTree(root.right)
            return new_root
        else:
            return None
