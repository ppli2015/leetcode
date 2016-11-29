# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = head
        if temp:
            while temp and temp.val == val:
                temp = temp.next
            head = temp
            while temp:
                while temp.next and temp.next.val == val:
                    temp.next = temp.next.next
                temp = temp.next
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)
temp = head
while temp:
    print temp.val
    temp = temp.next
print '=' * 10
test = Solution()
new = test.removeElements(head, 2)
temp = new
while temp:
    print temp.val
    temp = temp.next
