# -*-coding:cp936-*-
__author__ = 'lpp'


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.remove(self.queue[0])

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue == []


test = Queue()
print test.empty()
test.push(1)
print test.peek()