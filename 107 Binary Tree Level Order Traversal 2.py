# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root:
            result = []
            q = [root]
            while q:
                new_q = []
                result.append([n.val for n in q])
                for node in q:
                    if node.left:
                        new_q.append(node.left)
                    if node.right:
                        new_q.append(node.right)
                q = new_q
            return result[::-1]
        else:
            return []


test = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = None
root.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(5)
print test.levelOrderBottom(root)
