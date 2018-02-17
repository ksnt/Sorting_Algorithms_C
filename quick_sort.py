# Note: In this program, pivot value is selected from the first element of a given list 
#       This is not a general case. As in we can select the pivot value randomly.
# Note2:Algorithm is very simple but code is a little complicated

# ksnt

def quick_sort(a_list):
	""" helper function """
	quick_sort_helper(a_list,0,len(a_list)-1)


def quick_sort_helper(a_list,first,last):
    if first < last:
    	
    	split_point = partition(a_list,first,last)

    	quick_sort_helper(a_list,first,split_point - 1)
    	quick_sort_helper(a_list,split_point + 1, last)

def partition(a_list, first, last):

	pivoit_value = a_list[first] # Now choosing the first element as a pivot value

	left_mark  = first + 1
	right_mark = last

	done = False
	while not done:
		while left_mark <= right_mark and a_list[left_mark] <= pivoit_value:
			left_mark = left_mark + 1
		while a_list[right_mark] >= pivoit_value and right_mark >= left_mark and right_mark >= left_mark:
			right_mark = right_mark - 1
		if right_mark < left_mark:
			done = True
		else:
			temp = a_list[left_mark]
			a_list[left_mark] = a_list[right_mark]
			a_list[right_mark] = temp

	temp = a_list[first]
	a_list[first] = a_list[right_mark]
	a_list[right_mark] = temp

	return right_mark


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)