# Python program to calculate Prime numbers and subsequently Prime Factors

"""
Usage: Prime-numbers.py

Generates a sequence of Prime numbers up to the given number (n)
and also generates Prime factors for any user given number

At prompt, enter only numbers

Options
-------

-h or help		Displays this message

"""

from sys import argv, exit
import numpy as np


def prime(num):
	primeNumbers = []
	for i in np.arange(num+1):
		count_zero = 0
		if i >= 2:
			value = i
			for j in np.arange(1, value+1):
				rem = value % j
				if rem == 0:
					count_zero = count_zero + 1
					if count_zero >= 3:
						break
		if count_zero == 2:
			primeNumbers.append(i)
	
	return primeNumbers


def factor(facNum):
	primeFactors = []
	for pN in primeNumbersArray:
		while True:
			if (facNum % pN) == 0:
				facValue = facNum / pN
				primeFactors.append(pN)
				facNum = facValue
			else:
				break

	return primeFactors

if len(argv) > 1:
	print(__doc__)
	exit(0)

while True:
	number = raw_input("Enter the number: ")
	try:
		n = int(number)
		break
	except:
		print "Error: Enter only numbers"
		continue

primeNumbers = prime(n)
print "List of Prime Numbers up to %d:" % (n)
print primeNumbers
primeNumbersArray = np.array(primeNumbers)

while True:
	pFNum = raw_input("\nNow enter any other number to obtain the Prime Factors: ")
	try:
		pFNumber = int(pFNum)
		break
	except:
		print "Error: Enter only numbers"

if pFNumber in primeNumbersArray:
	print "Its a Prime!"
else:
	primeFactors = factor(pFNumber)
	if len(primeFactors) < 2:
		print ("Your Prime Numbers list is too short to obtain the prime factors",
"Regenerate the Prime Numbers list")
	else:
		print "The Prime Factors for %d are:" %(pFNumber)
		print primeFactors
