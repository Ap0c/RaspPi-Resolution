RaspPi-Resolution
=================

A command line Python program to alter the resolution of the Raspberry Pi. Can be used to change the resolution and overscan settings.

WARNING: This script will modify your boot config file, meaning that if something goes wrong your Pi may become unbootable and require a reflash of the SD card.

Why?
====

When you first boot up the Pi it's unlikely to be in the resolution you want. Changing it requires manually editing the config file and rebooting, which is a pain, particularly if you don't get it right first time. This program aims to simplify the process.
