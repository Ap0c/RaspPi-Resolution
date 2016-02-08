# ----- Imports ----- #

import subprocess


# ----- Setup ----- #

RES_FILES = {
	't': 'resolution-options-tv.txt',
	'm': 'resolution-options-monitor.txt'
}

HDMI_GROUPS = {
	't': 1,
	'm': 2
}

TV_MODES = 59
MON_MODES = 86

# CFG_FILE = '/boot/config.txt'
CFG_FILE = './test_config.txt'


# ----- Functions ----- #

def save_restart():

	"""Restarts the pi."""

	print('Rebooting...')

	subprocess.call(["reboot"])


def update_params(cfg, params):

	"""Updates the parameters in the config file, and appends new ones."""

	to_update = list(params.keys())

	for line_no, line in enumerate(cfg):

		for param, value in params.items():

			if param in line:

				cfg[line_no] = '{}={}\n'.format(param, value)
				to_update.remove(param)

	for param in to_update:
		cfg.append('{}={}\n'.format(param, params[param]))

	return cfg


def update_config(params):

	"""Updates the config file with new parameters."""

	with open(CFG_FILE, 'r') as cfg_in:
		cfg = cfg_in.readlines()

	cfg = update_params(cfg, params)

	with open(CFG_FILE, 'w') as cfg_out:
		cfg_out.writelines(cfg)


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

	update_config({
		'hdmi_mode': res,
		'hdmi_group': HDMI_GROUPS[screen]
	})


def print_overscan():

	"""Prints current overscan settings."""

	settings = {}

	with open(CFG_FILE, 'r') as cfg:

		for line in cfg:

			if "overscan" in line:

				param, value = line.split('=')
				param = param[9:]
				settings[param] = value.strip()

	for setting, value in settings.items():
		print(' - {} = {}'.format(setting, value))


def overscan_info():

	"""Prints some information about overscan."""

	print('\nOverscan changes the size of the image on screen.',
		'Positive numbers reduce the image size, increasing the black borders.',
		'Negative numbers increase the image size, reducing the black borders.')

	print('\nYour current overscan values are:')
	print_overscan()


def overscan():

	"""Alters the overscan/underscan of the display."""

	overscan_info()


def perform_action(option):

	"""Runs the option chosen by the user."""

	if option == 'r':
		resolution()
	elif option == 'o':
		overscan()
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
