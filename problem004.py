#!/usr/bin/python

import math

print 'Solving Problem 4'

def is_palindrome(number):
	return str(number) == str(number)[::-1]

start_left_number = 999
start_right_number = 999
largest = 0

while (start_left_number > 99):
	while (start_right_number > 99 and start_left_number * start_right_number > largest):
		if is_palindrome(start_left_number * start_right_number):
			largest = start_left_number * start_right_number
			break
		start_right_number = start_right_number - 1
	start_right_number = start_left_number
	start_left_number = start_left_number - 1

print 'Largest palindrome = ' + str(largest)