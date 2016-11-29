# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            slow = head
            fast = head
            while slow.next and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            if fast.next:
                # even
                last = slow.next
                pre = last.next
                while pre:
                    temp = pre.next
                    pre.next = last
                    last = pre
                    pre = temp

                left = head
                right = last
                while left != slow:
                    if left.val != right.val:
                        return False
                    else:
                        left = left.next
                        right = right.next
                if left.val == right.val:
                    return True
                else:
                    return False
            else:
                # odd
                last = slow
                pre = last.next
                while pre:
                    temp = pre.next
                    pre.next = last
                    last = pre
                    pre = temp
                left = head
                right = last
                while left != slow:
                    if left.val != right.val:
                        return False
                    else:
                        left = left.next
                        right = right.next
                return True
        else:
            return True


head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
test = Solution()
print test.isPalindrome(head)
