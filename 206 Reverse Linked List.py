#-*-coding:cp936-*-
__author__ = 'lpp'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        if head.next!=None:
            old = head.next
            new = head
            while old!=None:
                temp = ListNode(old.val)
                temp.next = new
                new = temp
                old = old.next
            head.next = None
            head = new
        return head

test = Solution()
a = ListNode(0)
temp = a
for i in range(1,10):
    temp.next = ListNode(i)
    temp = temp.next
temp = a
while temp!=None:
    print temp.val
    temp = temp.next
print '========='

result = test.reverseList(a)
temp = result
while temp!=None:
    print temp.val
    temp = temp.next