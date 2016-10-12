# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            q = [root]
            while q:
                new_q = []
                for node in q:
                    if node != None:
                        if node.left:
                            new_q.append(node.left)
                        else:
                            new_q.append(None)
                        if node.right:
                            new_q.append(node.right)
                        else:
                            new_q.append(None)
                for i in range(len(new_q) / 2):
                    if new_q[i] and new_q[len(new_q) - 1 - i]:
                        if new_q[i].val == new_q[len(new_q) - 1 - i].val:
                            pass
                        else:
                            return False
                    elif new_q[i] == None and new_q[len(new_q) - 1 - i] == None:
                        pass
                    else:
                        return False
                q = new_q
            return True
        else:
            return True


test = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = None
root.right = TreeNode(2)
root.right.left = None
root.right.right = TreeNode(5)
print test.isSymmetric(root)
