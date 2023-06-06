#!/usr/bin/python3
for num in range(ord('z'), ord('a')-1, -1):
    if num % 2 == 0:
        print('{}'.format(chr(num)), end='')
    else:
        print('{}'.format(chr(num - 32)), end='')
