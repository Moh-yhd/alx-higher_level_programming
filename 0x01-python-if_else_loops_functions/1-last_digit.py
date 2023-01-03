#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number < 0:
    last_digit = -(-(number) % 10)
else:
    last_digit = number % 10
print("last digit of {:d} is".format(number), end=' ')
if last_digit < 6 and last_digit != 0:
    print("{:d} and is less than 6 and not 0".format(last_digit))
elif last_digit == 0:
    print("{:d} and is 0".format(last_digit))
elif last_digit > 5:
    print("{:d} and is greater than 5".format(last_digit))
