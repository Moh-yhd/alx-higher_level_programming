#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = -1 * ((-1 * number) % 10)
else:
    last_digit = number % 10
print("last digit of {} is".format(number), end=' ')
if last_digit < 6 and last_digit != 0:
    print("{} and is less than 6 and not 0".format(last_digit))
elif last_digit == 0:
    print("{} and is 0".format(last_digit))
elif last_digit > 5:
    print("{} and is greater than 5".format(last_digit))
