#-*-coding:cp936-*-
__author__ = 'lpp'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next



a = ListNode(0)
a.next=ListNode(1)
temp = a
while temp!=None:
    print temp.val
    temp = temp.next
print '=========='
test = Solution()
test.deleteNode(a)
temp = a
while temp!=None:
    print temp.val
    temp = temp.next