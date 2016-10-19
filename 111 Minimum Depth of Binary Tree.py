#-*-coding:cp936-*-
__author__ = 'lpp'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            result = []
            templist = [root]
            while templist[-1].left or templist[-1].right:
                if templist[-1].left:
                    templist.append(templist[-1].left)
                else:
                    templist.append(templist[-1].right)

            r = []
            for i in templist:
                r.append(i.val)
            result.append(len(r))
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
                        result.append(len(r))
            return min(result)

        else:
            return 0

    def minDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            q = [root]
            depth = 1
            while q:
                new_q = []
                for node in q:
                    if node.left == None and node.right == None:
                        return depth
                    else:
                        if node.left:
                            new_q.append(node.left)
                        if node.right:
                            new_q.append(node.right)
                depth += 1
                q = new_q
        else:
            return 0



test = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = None
root.right = TreeNode(3)
# root.right.left = None
# root.right.right = TreeNode(5)
print test.minDepth(root)
print test.minDepth2(root)