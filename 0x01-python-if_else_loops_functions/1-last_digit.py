#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number < 0:
    last_digit = -(-(number) % 10)
else:
    last_digit = number % 10
print(f"last digit of {number} is", end=' ')
if last_digit < 6 and last_digit != 0:
    print(f"{last_digit:d} and is less than 6 and not 0")
elif last_digit == 0:
    print(f"{last_digit:d} and is 0")
elif last_digit > 5:
    print(f"{last_digit:d} and is greater than 5")
