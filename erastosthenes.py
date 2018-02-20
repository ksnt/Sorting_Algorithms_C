# Sieve of Eratosthenes
# ksnt

# Algorithm
# 1.Generate a list in which the numbers from 2 to n are included
# 2.The head element of the numbers (m) is added to another list for primes
# 3.Drop the numbers which can be divided by m
# 4.Repeat 2-3 till m+1 < sqrt(n)
# 5.The remaining numbers in the list generated first are added to the list for primes

# Example
# $ python erastosthenes.py 
# Please enter an integer:
# 10
# The result is:
# [2, 3, 5, 7]

import math

def erastosthenes(n):
	seq = [i for i in range(2,n+1)]
	primes = []
	#print(seq[0])
	while(seq[0] < math.sqrt(n)):
		primes.append(seq[0])
		for e in seq:
			if e % seq[0] == 0 and e != seq[0]:
				seq.remove(e)
		del seq[0]	
	#print(seq)
	primes = primes + seq
	return primes

print('Please enter an integer:')
n = int(input())
print("The result is:")
print(erastosthenes(n))