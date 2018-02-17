# Compare the execusion time to make list
# ksnt

""" result
$ python comp_sp_ds.py 
concat  3.5752507249999326 miliseconds
append  0.20047717099805595 miliseconds
comprehension  0.08130871100001968 miliseconds
list range  0.042281909998564515 miliseconds

list range < comprehension < append < concat

"""

import timeit

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

# measure time to execute code above
t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000),"miliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000),"miliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000),"miliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000),"miliseconds")