#!/usr/bin/python

print 'Solving Problem 2'

firstNumber = 1
secondNumber = 2
count = 0
runningSum = 0

# Loop until we break 4 million
while (secondNumber < 4000000):
	# Every third iteration will be an even number so add it
	if (count == 0):
		runningSum += secondNumber

	# Move on to next numbers
	tempNumber = secondNumber
	secondNumber = firstNumber + secondNumber
	firstNumber = tempNumber

	# Increment count
	count += 1
	if (count == 3):
		count = 0

print 'Solution is ' + str(runningSum)