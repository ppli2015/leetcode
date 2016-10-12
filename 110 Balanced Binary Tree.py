# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if abs(self.height(root.left) - self.height(root.right)) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return True

    def height(self, root):
        if root:
            return 1 + max(self.height(root.left), self.height(root.right))
        else:
            return 0

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = None
root.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(5)
test = Solution()
print test.isBalanced(root)