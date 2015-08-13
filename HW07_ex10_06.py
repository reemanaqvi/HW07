# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

"""This functionr returns True only if the list provided is already sorted.
"""

def is_sorted(list_):
	if list_ == sorted(list_):		# Checks whether the list is the same as its sorted version
		return True
	else:
		return False


############################################################	
def main():
	pass

	# test = [5,1,2]
	# print is_sorted(test)
	

if __name__ == '__main__':
    main()
############################################################
