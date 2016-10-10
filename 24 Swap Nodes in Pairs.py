# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next != None:
            temp = head
            head = head.next
            temp.next = head.next
            head.next = temp
            while temp.next != None:
                temp2 = temp.next
                if temp2.next != None:
                    temp.next = temp2.next
                    temp = temp.next
                    temp2.next = temp.next
                    temp.next = temp2
                    temp = temp.next
                else:
                    break
        return head


test = Solution()

a = ListNode(1)
temp = a
for i in range(2, 10):
    temp.next = ListNode(i)
    temp = temp.next

temp = a
while temp != None:
    print temp.val
    temp = temp.next
print '========='

result = test.swapPairs(a)
temp = result
while temp != None:
    print temp.val
    temp = temp.next
print '========='
