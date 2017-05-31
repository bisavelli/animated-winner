# animated-winner
This python script does the following:
1. takes a device template in Jinja2 format (see templates folder for example)
2. uses a device/host variable list to populate variable locations in said templates (see hosts folder for example)
3. renders a configuration file based on parts 1 and 2 in root directory based on hostname provided in arguments

Usage is as follows:

python dtp.py <device/host> <template>

Enjoy!
