# Binary Search
# ksnt

# Example
# (1)
# $ python binary_search.py 
# Enter an integer you want to look for:
# 10
# Enter the numbers in a list: 100 99 88 10 34
# Found!
# (2)
# $ python binary_search.py 
# Enter an integer you want to look for:
# 10
# Enter the numbers in a list: 1 2 9 100 99 99 22
# Not Found

def binary_search(seq,v,l,r):
	while(r >= l):
		m = (l + r) // 2
		if v == seq[m]:
			print("Found!")
			return m
		if v < seq[m]:
			r = m-1
		else:
			l = m+1
	print("Not Found")

#num = 10
#seq = [1,3,100,10]

print('Enter an integer you want to look for:')
num = int(input())
seq=list(map(int,input("Enter the numbers in a list: ").split()))
seq.sort()
binary_search(seq,num,l=0,r=len(seq))