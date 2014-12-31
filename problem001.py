#!/usr/bin/python

print 'Solving Problem 1'

# Find the number of times multiples of 3, 5, and 15 appear
nThree = (1000 - 1) // 3
nFive = (1000 - 1) // 5
nFifteen = (1000 - 1) // 15

# Calculate the arithmetic sum for the appearances
sumsThree = 3 * nThree * (nThree + 1) / 2
sumsFive = 5 * nFive * (nFive + 1) / 2
sumsFifteen = 15 * nFifteen * (nFifteen + 1) / 2

print 'Sums of three = ' + str(sumsThree)
print 'Sums of five = ' + str(sumsFive)
print 'Sums of fifteen = ' + str(sumsFifteen)

# Total sum is three and five minus 15 (removes duplicates)
totalSum = sumsThree + sumsFive - sumsFifteen

print 'Sum total = ' + str(totalSum)