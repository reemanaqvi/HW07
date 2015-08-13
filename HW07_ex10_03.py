# I want to be able to call cumulative_sum from main w/ various lists and 
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]



"""This function returns a new list where every number in the list is the cumulative sum of the previous numbers
"""

def cumulative_sum(list_):
	list_sum = []					# Initiates list
	x = 0
	for item in list_:
		last_nr = item + x			# Adds current number with previous numbers
		list_sum.append(last_nr)	# Adds cumulative number to end of list_sum
		x = last_nr					# So that the itiration uses every successive cumulative sum
	return list_sum
	print list_sum
	
############################################################	
def main():
	pass
	# prime_numbers = [1,2,3,5,7,11]
	# print cumulative_sum(prime_numbers)
	

if __name__ == '__main__':
    main()
############################################################
