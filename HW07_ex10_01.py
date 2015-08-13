# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

"""Nesting a list in nested_sum that returns a list with last index being the sum of all previous numbers
"""
nested_list = [-4,[-5,6], 4]

def nested_sum(nested_list):
	total_sum = 0
	for item in nested_list:
		if type(item) == type(list()):
			total_sum += nested_sum(item)
		else:
			total_sum += item
	return total_sum

nested_sum(nested_list)


def main():
    pass

if __name__ == '__main__':
    main()