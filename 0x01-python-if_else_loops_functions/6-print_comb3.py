#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        if num2 < 9 or num1 < 8:
            print("{:d}".format(num1) + "{:d}".format(num2), end=", ")
        else:
            print("{:d}".format(num1) + "{:d}".format(num2))
