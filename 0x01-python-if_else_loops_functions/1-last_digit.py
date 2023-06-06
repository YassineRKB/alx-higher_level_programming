#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
	last = last * -1
if last < 6 and last != 0 and last > 0:
	print("Last digit of {number:d} is {last:d} and is less than 6 and not 0")
elif last < 6 and last != 0 and last < 0:
	print("Last digit of {number:d} is {last:d} and is less than 6 and not 0")
elif last == 0:
	print("Last digit of {} is {} and is 0".format(number, last))
elif last > 5:
	print("Last digit of {} is {} and is greater than 5".format(number, last))
