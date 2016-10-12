# -*-coding:utf-8-*-
__author__ = 'lpp'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            count = 0
            q = [root]
            while q:
                new_q = []
                for node in q:
                    if node ==None:
                        continue
                    if node.left and node.right:
                        # count += node.left.val
                        new_q.append(node.left)
                        new_q.append(node.right)
                    elif node.left:
                        new_q.append(node.left)
                        new_q.append(None)
                    elif node.right:
                        new_q.append(None)
                        new_q.append(node.right)
                    else:
                        if q.index(node) % 2 == 0 and node != root:
                            count += node.val
                q = new_q
            return count


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = None
root.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(5)
test = Solution()
print test.sumOfLeftLeaves(root)
