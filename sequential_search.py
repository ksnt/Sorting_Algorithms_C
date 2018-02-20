# Sequential Search
# ksnt

# This program find the first element and whose index in the given list
# Example
# $python sequential_search.py 
#  Enter an integer you want to look for:
#  10
#  Enter the numbers in the list: 3 90 100 10 29 10
#  Found. It is the 4 th element in the list.

def sequential_search(integer,sequence):
	#print(sequence)
	for (i,e) in enumerate(sequence):
		if e == integer:
			print("Found. It is the", i+1, "th element in the list.")
			return
	print("Not found.")


print('Enter an integer you want to look for:')
n = int(input())
seq=list(map(int,input("Enter the numbers in the list: ").split()))
#print(seq)
sequential_search(n,seq)