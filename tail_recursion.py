# Tail Recursion
# ksnt

# You can easily find many examples using tail recursion anywhere.

## A.Factorial function 

# Recursive
def factorial1(n):
	if n == 0:
	    return 1 
	else:
		return n * factorial1(n-1)

# Another approach (Iterative recursion)
def factorial2(n,total=1):
	if n == 1:
		return total
	else:
		return factorial2(n-1, n * total)


## B.Fibonacci sequence

#1.Recursive
#This is a simple way but inefficient
#because duplicated operations are calculated
def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

#2.Tail Recursive
# current fibonacci number  : a
# previous fibonacci number : b
def fib_tail(n,a=1,b=0):
	if n < 1:
		return a
	return fib_tail(n-1,a+b,a)
