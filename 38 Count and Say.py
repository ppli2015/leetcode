# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n > 0:
            s = '1'
            q = list(s)
            for i in range(2, n + 1):
                new_q = []
                temp = 0
                count = 1
                while temp < len(q):
                    if temp + 1 < len(q):
                        if q[temp + 1] == q[temp]:
                            count += 1

                        else:
                            new_q.append(str(count))
                            new_q.append(q[temp])
                            count = 1
                        temp += 1
                    else:
                        new_q.append(str(count))
                        new_q.append(q[temp])
                        temp += 1
                q = new_q
            return ''.join(q)
        else:
            return ''


test = Solution()
print test.countAndSay(8)
