# -*-coding:cp936-*-
__author__ = 'lpp'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        else:
            temp = head
            print temp
            dic = {}
            dic[temp.val] = [temp]
            while temp.next:
                temp = temp.next
                if dic.has_key(temp.val):
                    for node in dic[temp.val]:
                        if node == temp:
                            return True
                    dic[temp.val].append(temp)
                else:
                    dic[temp.val] = [temp]
            return False


test = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
print test.hasCycle(head)
