#-*-coding:cp936-*-
__author__ = 'lpp'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        else:
            temp = head
            while temp.next!=None:
                if temp.next.val==temp.val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
        return head

test = Solution()
a = ListNode(0)
temp = a
for i in [1,1,2,3,3,4,4,4,4]:
    temp.next = ListNode(i)
    temp = temp.next
temp = a
while temp!=None:
    print temp.val
    temp = temp.next
print '========='

result = test.deleteDuplicates(a)
temp = result
while temp!=None:
    print temp.val
    temp = temp.next