#!/usr/bin/env python3
# COPYRIGHT AYDAR N. (me@aydar.media)
#
# 2022
#

import sys

RED = "\033[31m"
GRN = "\033[32m"
ORG = "\033[33m"
CYN = "\033[36m"
BLD = "\033[1m"
RES = "\033[0m"

def my_except_hook(exctype, value, traceback):
	if exctype is KeyboardInterrupt:
		print("Q!")
		return
	print(f'{RED + BLD}FATAL:{RES} {value}')
	exit(1)
sys.excepthook = my_except_hook
