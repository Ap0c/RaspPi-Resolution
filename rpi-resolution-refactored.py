# ----- Imports ----- #

# import subprocess


# ----- Functions ----- #

def perform_action(option):

	"""Runs the option chosen by the user."""

	if option == 'r':
		# resolution()
		pass
	elif option == 'o':
		# overscan()
		pass
	elif option == 's':
		# restart()
		pass
	elif option == 'q':
		pass
	else:
		return False

	return True


def user_input():

	"""Asks the user what they wish to do, then performs that action."""

	print('Welcome to rpi-resolution.\n',
		"'r' - change resolution",
		"'o' - change overscan",
		"'s' - save and restart",
		"'q' - quit\n", sep='\n')

	choice = input('What would you like to do: ')

	if perform_action(choice):
		print('Done.')
	else:
		print('Error: unrecognised option')


# ----- Run ----- #

if __name__ == '__main__':

	user_input()
