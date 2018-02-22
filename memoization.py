# Memoization
# ksnt

# Reference
# https://www.python-course.eu/python3_memoization.php

# 1.Fibonacci sequence
# 1.1. Normal version (recursive, according to mathematical definition)

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

# 1.2. Memoization version

def memoize(f):
	memo = {} # using dictionary
	def helper(x):
		if x not in memo:
			memo[x] = f(x)
		return memo[x]
	return helper

fib = memoize(fib)

# we can use decorator

@memoize
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print(fib(40))

# we can also use Memoize class with decorator

class Memoize:
	def __init__(self,fn):
		self.fn = fn
		self.memo = {}
	def __call__(self,*args):
		if args not in self.memo:
			self.memo[args] = self.fn(*args)
		return self.memo[args]

@Memoize
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

		
# 2.Factorial
# 2.1.Normal version (recursive)

def fact_normal(n):
	if n == 0:
		return 1
	else:
		return n * fact_normal(n-1)

# 2.2.Memoization version

@Memoize
def fact_normal(n):
	if n == 0:
		return 1
	else:
		return n * fact_normal(n-1)


#print('Enter a positive integer you want to look for:')
#n = int(input())
#print("The result of normal version is:", fact_normal(n))