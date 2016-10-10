# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            if l1.val < l2.val:
                result = ListNode(l1.val)
                temp1 = l1.next
                temp2 = l2
            else:
                result = ListNode(l2.val)
                temp1 = l1
                temp2 = l2.next
            temp = result
            while temp1 != None and temp2 != None:
                if temp1.val < temp2.val:
                    temp.next = ListNode(temp1.val)
                    temp1 = temp1.next
                else:
                    temp.next = ListNode(temp2.val)
                    temp2 = temp2.next
                temp = temp.next
            if temp1 == None:
                temp.next = temp2
            else:
                temp.next = temp1
        return result


test = Solution()

a = ListNode(0)
b = ListNode(0)
temp = a
temp2 = b
for i in range(1, 10):
    temp.next = ListNode(i)
    temp = temp.next
    temp2.next = ListNode(i + 2)
    temp2 = temp2.next
temp = a
while temp != None:
    print temp.val
    temp = temp.next
print '========='
temp = b
while temp != None:
    print temp.val
    temp = temp.next
print '========='

result = test.mergeTwoLists(a, b)
temp = result
while temp != None:
    print temp.val
    temp = temp.next
print '========='
