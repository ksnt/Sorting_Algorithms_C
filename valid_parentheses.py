def valid_parenthes(given_str):
	sum = 0
	for s in given_str:
		if sum < 0:
			print("not valid")
			return 0
		elif s == '(':
			sum += 1
		elif s == ')':
			sum -= 1
		else:
			pass
	if sum != 0:
	    print("not valid")
	    return 0
	print("valid")

given_str = "(()))"
valid_parenthes(given_str)