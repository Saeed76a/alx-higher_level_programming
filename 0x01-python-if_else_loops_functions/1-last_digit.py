#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if number < 0:
    ld = 10 - ld
print("Last digit of", end=' ')
if ld > 5:
    print(f"{number:d} is {ld:d} and is greater than 5")
elif ld == 0:
    print(f"{number:d} is {ld:d} and is 0")
else:
    print(f"{number:d} is {ld:d} and is less than 6 and not 0")
