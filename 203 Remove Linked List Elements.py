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
            while temp and temp.next and temp.next.val == val:
                temp.next = temp.next.next
                temp = temp.next
        return head

    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head:
            dummy = ListNode(0)
            dummy.next = head
            pre = dummy
            while head:
                if head.val == val:
                    pre.next = head.next
                    head = pre
                pre = head
                head = head.next
            return dummy.next
        else:
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
