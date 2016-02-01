"""Note: when running this program it is necessary to provide superuser permissions,
as it requires access to the config.txt file and the ability to reboot the pi.
If running in the terminal, use the sudo command: 'sudo python <path to program>'."""

import subprocess

#Main function, asks what the user wants the program to do.

def what():
	firstoption = raw_input("What would you like to do? Enter 'r' for change resolution, 'o' for change overscan, 's' for save and restart or 'q' for quit: ")
	if firstoption == 'r':
		resolution()
	elif firstoption == 'o':
		overscan()
	elif firstoption == 's':
		restart()
	elif firstoption == 'q':
		SystemExit(0)
	else:
		print "That was not an option."
		what()

#Alters the resolution of the display.

def resolution():
	print "Your current resolution is:"
	subprocess.call(["tvservice", "-s"])

	screentype = raw_input("What type of screen are you using? Enter 't' for TV or 'm' for computer monitor: ")
	if screentype == 't':
		editfile("hdmi_group", 1)
		resolutionoptions(screentype) 
	elif screentype == 'm':
		editfile("hdmi_group", 2)
		resolutionoptions(screentype)
	else:
		print "I'm sorry, that was not one of the options."
		resolution()

	screenres = raw_input("What resolution do you want? Please enter the mode number next to the resolution listed above: ")
	editfile("hdmi_mode", screenres)

	what()

#Changes the overscan to user-inputted values.

def overscan():
	print "Your current overscan settings are:\n"
	with open('/boot/config.txt') as f:
		for line in f:
			if "overscan" in line:
				print line

	top = raw_input("Would you like to change your top overscan? Press y for yes or any other key for no: ")
	if top == 'y':
		amount = raw_input("How much overscan do you want? Positive numbers reduce the image size on the screen, negative numbers increase it, reducing the size of the black borders: ")
		editfile("overscan_top", amount)

	bottom = raw_input("Would you like to change your bottom overscan? Press y for yes or any other key for no: ")
	if bottom == 'y':
		amount = raw_input("How much overscan do you want? Positive numbers reduce the image size on the screen, negative numbers increase it, reducing the size of the black borders: ")
		editfile("overscan_bottom", amount)

	left = raw_input("Would you like to change your left overscan? Press y for yes or any other key for no: ")
	if left == 'y':
		amount = raw_input("How much overscan do you want? Positive numbers reduce the image size on the screen, negative numbers increase it, reducing the size of the black borders: ")
		editfile("overscan_left", amount)

	right = raw_input("Would you like to change your right overscan? Press y for yes or any other key for no: ")
	if right == 'y':
		amount = raw_input("How much overscan do you want? Positive numbers reduce the image size on the screen, negative numbers increase it, reducing the size of the black borders: ")
		editfile("overscan_right", amount)

	what()

#Restarts the pi.

def restart():
	configfile = open('/boot/config.txt', 'r')
	print "Your config file now looks like this:\n" + configfile.read()
	configfile.close()

	print "Rebooting...\n"
	subprocess.call(["reboot"])

#Generic function for editing part of the config file.

def editfile(parameter, modification):
	with open('/boot/config.txt') as f:
		data = f.readlines()

	writenew = 1

	for num, line in enumerate(data):
		if parameter in line:
			data[num] = parameter + "=" + str(modification) +"\n"
			writenew = 0

	if writenew == 1:
		data.append(parameter + "=" + str(modification) +"\n")

	with open('/boot/config.txt', 'w') as file:
		for line in data:
			file.write(line)

#Prints out all possible resolution options.

def resolutionoptions(n):
	if n == 't':
		print "The possible display resolutions can be seen below:\nhdmi_mode=1    VGA\nhdmi_mode=2    480p  60Hz\nhdmi_mode=3    480p  60Hz  H\nhdmi_mode=4    720p  60Hz\nhdmi_mode=5    1080i 60Hz\nhdmi_mode=6    480i  60Hz\nhdmi_mode=7    480i  60Hz  H\nhdmi_mode=8    240p  60Hz\nhdmi_mode=9    240p  60Hz  H\nhdmi_mode=10   480i  60Hz  4x\nhdmi_mode=11   480i  60Hz  4x H\nhdmi_mode=12   240p  60Hz  4x\nhdmi_mode=13   240p  60Hz  4x H\nhdmi_mode=14   480p  60Hz  2x\nhdmi_mode=15   480p  60Hz  2x H\nhdmi_mode=16   1080p 60Hz\nhdmi_mode=17   576p  50Hz\nhdmi_mode=18   576p  50Hz  H\nhdmi_mode=19   720p  50Hz\nhdmi_mode=20   1080i 50Hz\nhdmi_mode=21   576i  50Hz\nhdmi_mode=22   576i  50Hz  H\nhdmi_mode=23   288p  50Hz\nhdmi_mode=24   288p  50Hz  H\nhdmi_mode=25   576i  50Hz  4x\nhdmi_mode=26   576i  50Hz  4x H\nhdmi_mode=27   288p  50Hz  4x\nhdmi_mode=28   288p  50Hz  4x H\nhdmi_mode=29   576p  50Hz  2x\nhdmi_mode=30   576p  50Hz  2x H\nhdmi_mode=31   1080p 50Hz\nhdmi_mode=32   1080p 24Hz\nhdmi_mode=33   1080p 25Hz\nhdmi_mode=34   1080p 30Hz\nhdmi_mode=35   480p  60Hz  4x\nhdmi_mode=36   480p  60Hz  4xH\nhdmi_mode=37   576p  50Hz  4x\nhdmi_mode=38   576p  50Hz  4x H\nhdmi_mode=39   1080i 50Hz  reduced blanking\nhdmi_mode=40   1080i 100Hz\nhdmi_mode=41   720p  100Hz\nhdmi_mode=42   576p  100Hz\nhdmi_mode=43   576p  100Hz H\nhdmi_mode=44   576i  100Hz\nhdmi_mode=45   576i  100Hz H\nhdmi_mode=46   1080i 120Hz\nhdmi_mode=47   720p  120Hz\nhdmi_mode=48   480p  120Hz\nhdmi_mode=49   480p  120Hz H\nhdmi_mode=50   480i  120Hz\nhdmi_mode=51   480i  120Hz H\nhdmi_mode=52   576p  200Hz\nhdmi_mode=53   576p  200Hz H\nhdmi_mode=54   576i  200Hz\nhdmi_mode=55   576i  200Hz H\nhdmi_mode=56   480p  240Hz\nhdmi_mode=57   480p  240Hz H\nhdmi_mode=58   480i  240Hz\nhdmi_mode=59   480i  240Hz H\nH means 16:9 variant (of a normally 4:3 mode).\n2x means pixel doubled (i.e. higher clock rate, with each pixel repeated twice)\n4x means pixel quadrupled (i.e. higher clock rate, with each pixel repeated four times)"
	else:
		print "The possible display resolutions can be seen below:\nhdmi_mode=1    640x350   85Hz\nhdmi_mode=2    640x400   85Hz\nhdmi_mode=3    720x400   85Hz\nhdmi_mode=4    640x480   60Hz\nhdmi_mode=5    640x480   72Hz\nhdmi_mode=6    640x480   75Hz\nhdmi_mode=7    640x480   85Hz\nhdmi_mode=8    800x600   56Hz\nhdmi_mode=9    800x600   60Hz\nhdmi_mode=10   800x600   72Hz\nhdmi_mode=11   800x600   75Hz\nhdmi_mode=12   800x600   85Hz\nhdmi_mode=13   800x600   120Hz\nhdmi_mode=14   848x480   60Hz\nhdmi_mode=15   1024x768  43Hz  DO NOT USE\nhdmi_mode=16   1024x768  60Hz\nhdmi_mode=17   1024x768  70Hz\nhdmi_mode=18   1024x768  75Hz\nhdmi_mode=19   1024x768  85Hz\nhdmi_mode=20   1024x768  120Hz\nhdmi_mode=21   1152x864  75Hz\nhdmi_mode=22   1280x768        reduced blanking\nhdmi_mode=23   1280x768  60Hz\nhdmi_mode=24   1280x768  75Hz\nhdmi_mode=25   1280x768  85Hz\nhdmi_mode=26   1280x768  120Hz reduced blanking\nhdmi_mode=27   1280x800        reduced blanking\nhdmi_mode=28   1280x800  60Hz\nhdmi_mode=29   1280x800  75Hz\nhdmi_mode=30   1280x800  85Hz\nhdmi_mode=31   1280x800  120Hz reduced blanking\nhdmi_mode=32   1280x960  60Hz\nhdmi_mode=33   1280x960  85Hz\nhdmi_mode=34   1280x960  120Hz reduced blanking\nhdmi_mode=35   1280x1024 60Hz\nhdmi_mode=36   1280x1024 75Hz\nhdmi_mode=37   1280x1024 85Hz\nhdmi_mode=38   1280x1024 120Hz reduced blanking\nhdmi_mode=39   1360x768  60Hz\nhdmi_mode=40   1360x768  120Hz reduced blanking\nhdmi_mode=41   1400x1050       reduced blanking\nhdmi_mode=42   1400x1050 60Hz\nhdmi_mode=43   1400x1050 75Hz\nhdmi_mode=44   1400x1050 85Hz\nhdmi_mode=45   1400x1050 120Hz reduced blanking\nhdmi_mode=46   1440x900        reduced blanking\nhdmi_mode=47   1440x900  60Hz\nhdmi_mode=48   1440x900  75Hz\nhdmi_mode=49   1440x900  85Hz\nhdmi_mode=50   1440x900  120Hz reduced blanking\nhdmi_mode=51   1600x1200 60Hz\nhdmi_mode=52   1600x1200 65Hz\nhdmi_mode=53   1600x1200 70Hz\nhdmi_mode=54   1600x1200 75Hz\nhdmi_mode=55   1600x1200 85Hz\nhdmi_mode=56   1600x1200 120Hz reduced blanking\nhdmi_mode=57   1680x1050       reduced blanking\nhdmi_mode=58   1680x1050 60Hz\nhdmi_mode=59   1680x1050 75Hz\nhdmi_mode=60   1680x1050 85Hz\nhdmi_mode=61   1680x1050 120Hz reduced blanking\nhdmi_mode=62   1792x1344 60Hz\nhdmi_mode=63   1792x1344 75Hz\nhdmi_mode=64   1792x1344 120Hz reduced blanking\nhdmi_mode=65   1856x1392 60Hz\nhdmi_mode=66   1856x1392 75Hz\nhdmi_mode=67   1856x1392 120Hz reduced blanking\nhdmi_mode=68   1920x1200       reduced blanking\nhdmi_mode=69   1920x1200 60Hz\nhdmi_mode=70   1920x1200 75Hz\nhdmi_mode=71   1920x1200 85Hz\nhdmi_mode=72   1920x1200 120Hz reduced blanking\nhdmi_mode=73   1920x1440 60Hz\nhdmi_mode=74   1920x1440 75Hz\nhdmi_mode=75   1920x1440 120Hz reduced blanking\nhdmi_mode=76   2560x1600       reduced blanking\nhdmi_mode=77   2560x1600 60Hz\nhdmi_mode=78   2560x1600 75Hz\nhdmi_mode=79   2560x1600 85Hz\nhdmi_mode=80   2560x1600 120Hz reduced blanking\nhdmi_mode=81   1366x768  60Hz\nhdmi_mode=82   1080p     60Hz\nhdmi_mode=83   1600x900        reduced blanking\nhdmi_mode=84   2048x1152       reduced blanking\nhdmi_mode=85   720p      60Hz\nhdmi_mode=86   1366x768        reduced blanking\n"

what()