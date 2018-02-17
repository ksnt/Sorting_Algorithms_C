# Compare the execusion time to make list
# ksnt

import timeit
import matplotlib
import matplotlib.pyplot as plt

# Import the Timer class
from timeit import Timer

def test1():
	""" addition of elements to list"""
	l = []
	for i in range(1000):
		l = l + [i]

def test2():
	""" append elements with list"""
	l = []
	for i in range(1000):
		l.append(i)

def test3():
	""" list comprehension"""
	l = [i for i in range(1000)]

def test4():
	""" directly make list from random numbers"""
	l = list(range(1000))

# measure time to execute the code above
t1 = Timer("test1()", "from __main__ import test1")
t1_result = t1.timeit(number=1000)
t1_label = "concat"
print("concat ",t1_result,"miliseconds")
t2 = Timer("test2()", "from __main__ import test2")
t2_result = t2.timeit(number=1000)
t2_label = "append"
print("append ",t2_result,"miliseconds")
t3 = Timer("test3()", "from __main__ import test3")
t3_result = t3.timeit(number=1000)
t3_label = "comprehension"
print("comprehension ",t3_result,"miliseconds")
t4 = Timer("test4()", "from __main__ import test4")
t4_result = t4.timeit(number=1000)
t4_label = "list range"
print("list range ",t4_result,"miliseconds")

N = 4
n = range(N)
plt.bar(n,list([t1_result,t2_result,t3_result,t4_result]))
plt.xticks(n, list([t1_label,t2_label,t3_label,t4_label]))
plt.show()