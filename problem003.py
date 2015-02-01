#!/usr/bin/python

import math

print 'Solving Problem 3'

start_number = 3
primes = []

current_number = start_number
original_number = 600851475143
stop_number = math.sqrt(original_number)
print 'Stop number is ' + str(stop_number)
while (current_number < stop_number):
	is_prime = True
	for prime in primes:
		if (current_number % prime == 0):
			is_prime = False
			break
	if (is_prime == True):
		primes.append(current_number)
	current_number = current_number + 2
current_number = primes.pop()
while (original_number % current_number != 0):
	current_number = primes.pop()

print 'Solution is ' + str(current_number)