# Sieve of Eratosthenes
# ksnt

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