# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp1 = head
        temp2 = temp1
        for i in range(n):
            temp2 = temp2.next
        if temp2:
            while temp2.next:
                temp2 = temp2.next
                temp1 = temp1.next
            temp1.next = temp1.next.next
            return head
        else:
            head = head.next
            return head


test = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(4)
root.next.next.next = ListNode(5)
temp = root
while temp:
    print temp.val
    temp = temp.next
root2 = test.removeNthFromEnd(root, 1)
temp = root2
while temp:
    print temp.val
    temp = temp.next
