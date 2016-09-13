# -*-coding:cp936-*-
__author__ = 'lpp'

num = 1000000000000
count = 1
while num > 0:
    num = num - 2 ** count
    count += 1
count -= 1
num = num + 2 ** count

s = ''
# count2=1
# while count2<=count:
for count2 in range(1, count + 1):
    yu = num % (2 ** count2)
    if yu <= 2 ** (count2 - 1) and yu != 0:
        s += '4'
    else:
        s += '7'
    count2 += 1
print s[::-1]
