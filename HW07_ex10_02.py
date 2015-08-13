"""Calling capitalize_nested from main w/ various lists and get returned a new nested list with all strings capitalized.
"""


colors = ['rEFd', ["orange", "pink"],'blue', 'green']

def capitalize_nested(colors):
	cap_colors = []
	for shade in colors:
		if type(shade) == type(list()):
			new_nestedlist = capitalize_nested(shade)
			cap_colors.append(new_nestedlist)
		else:
			a = shade.capitalize()
			cap_colors.append(a)

	return cap_colors

print capitalize_nested(colors)





# capitalize_nested()



# def main():
#     pass 
# if __name__ == '__main__':
#     main()