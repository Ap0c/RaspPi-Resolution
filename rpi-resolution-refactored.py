# ----- Imports ----- #

import subprocess


# ----- Setup ----- #

RES_FILES = {
	't': 'resolution-options-tv.txt',
	'm': 'resolution-options-monitor.txt'
}

TV_MODES = 59
MON_MODES = 86


# ----- Functions ----- #

def save_restart():

	"""Restarts the pi."""

	print('Rebooting...')

	subprocess.call(["reboot"])


def get_resolution(screen):

	"""Gets the resolution from the user."""

	print('What resolution would you like?')
	res = input('Enter an HDMI mode number from the list above: ')

	try:
		res = int(res)
	except ValueError:
		print('\nPlease enter a whole number.\n')
		return get_resolution(screen)

	modes = range(1, TV_MODES + 1) if screen is 't' else range(1, MON_MODES + 1)

	if res in modes:
		return res
	else:
		print('\nNo such resolution.\n')
		return get_resolution(screen)


def get_screen():

	"""Gets the screen type."""

	print('What type of screen are you using?')
	screen = input("'t' for TV, 'm' for computer monitor: ")

	if screen in ['t', 'm']:
		return screen
	else:

		print('\nNo such screen type.\n')
		return get_screen()


def print_resolutions(screen):

	"""Prints the resolution options for the user."""

	res_file = RES_FILES[screen]

	with open(res_file, 'r') as f:
		print(f.read())


def resolution():

	"""Alters the resolution of the display based on user choice."""

	# current_res = subprocess.call(['tvservice', '-s'])
	# print('Your current resolution is: {}\n'.format(current_res))

	screen = get_screen()
	print_resolutions(screen)
	res = get_resolution(screen)

	print(res)


def perform_action(option):

	"""Runs the option chosen by the user."""

	if option == 'r':
		resolution()
	elif option == 'o':
		# overscan()
		pass
	elif option == 's':
		# save_restart()
		pass
	elif option == 'q':
		pass
	else:
		return 'fail'

	return 'success'


def user_input():

	"""Asks the user what they wish to do, then performs that action."""

	print('Welcome to rpi-resolution.\n',
		"'r' - change resolution",
		"'o' - change overscan",
		"'s' - save and restart",
		"'q' - quit\n", sep='\n')

	choice = input('What would you like to do: ')

	result = perform_action(choice)

	if result == 'success':
		print('Done.')
	else:
		print('Error: unrecognised option')


# ----- Run ----- #

if __name__ == '__main__':

	user_input()
