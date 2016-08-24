# -*-coding:cp936-*-
__author__ = 'lpp'

# 理解题意
# 进位问题
# 最后检查是否有进位 5+5=10

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a1 = 0
        a2 = 0
        N1 = 0
        N2 = 0
        temp1 = l1
        temp2 = l2
        while temp1 != None:
            N1 += temp1.val * (10 ** a1)
            a1 += 1
            temp1 = temp1.next
        while temp2 != None:
            N2 += temp2.val * (10 ** a2)
            a2 += 1
            temp2 = temp2.next

        N3 = N1 + N2
        result = ListNode(N3 % 10)
        l3 = result
        N3 /= 10
        while N3 != 0:
            result.next = ListNode(N3 % 10)
            N3 /= 10
            result = result.next
        return l3

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        temp2 = l2
        result = ListNode(0)
        l3 = result
        add = 0
        while temp1 != None or temp2 != None:
            if temp1 != None:
                x = temp1.val
                temp1 = temp1.next
            else:
                x = 0
            if temp2 != None:
                y = temp2.val
                temp2 = temp2.next
            else:
                y = 0
            sum = x + y + add
            result.next = ListNode(sum % 10)
            result = result.next
            add = sum / 10
        if add > 0:
            result.next = ListNode(add)
        return l3.next


# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# l1 = ListNode(1)
# l1.next = ListNode(8)
# l2 = ListNode(0)

l1 = ListNode(5)
l2 = ListNode(5)

test = Solution()
result = test.addTwoNumbers2(l1, l2)
while result!=None:
    print result.val
    result = result.next
