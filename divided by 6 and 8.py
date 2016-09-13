#-*-coding:cp936-*-
__author__ = 'lpp'


def solution(n):
    if n%8==0:
        print '6: 0, 8: '+str(n/8)
        return n/8
    elif (n-6)%8==0:
        print '6: 1, 8: '+str((n-6)/8)
        return 1+(n-6)/8
    elif (n-12)%8==0:
        print '6: 2, 8: '+str((n-6)/8)
        return 2+(n-12)/8
    elif (n-18)%8==0:
        print '6: 3, 8: '+str((n-18)/8)
        return 3+(n-18)/8
    else:
        return -1

print solution(66)