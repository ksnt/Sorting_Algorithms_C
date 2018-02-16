# In this code, first find biggest element in the list, then set the number to the right edge

def selection_sort(a_list):
	for fill_slot in range(len(a_list)-1,0,-1):
		pos_of_max = 0
		for location in range(1,fill_slot + 1):
			if a_list[location] > a_list[pos_of_max]:
				pos_of_max = location
		# swap the element which has max value for the element which is on the right edge
		temp = a_list[fill_slot]
		a_list[fill_slot] = a_list[pos_of_max]
		a_list[pos_of_max] = temp

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)