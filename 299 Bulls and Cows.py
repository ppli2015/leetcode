# -*-coding:cp936-*-
__author__ = 'lpp'


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        secret = list(secret)
        guess = list(guess)
        i = 0
        while i < len(secret):
            if secret[i] == guess[i]:
                A += 1
                secret.remove(secret[i])
                guess.remove(guess[i])
            else:
                i += 1
        B = 0
        for i in list(set(secret) & set(guess)):
            B += min(secret.count(i), guess.count(i))
        return str(A) + 'A' + str(B) + 'B'


test = Solution()
print test.getHint('1122', '0001')
