#!/usr/bin/env python3
'''''''''''''''''''''''''''''
COPYRIGHT LESTER COVEY (me@lestercovey.ml),
2022

'''''''''''''''''''''''''''''
import sys

RED = "\033[31m"
GRN = "\033[32m"
ORG = "\033[33m"
CYN = "\033[36m"
BLD = "\033[1m"
RES = "\033[0m"

def my_except_hook(exctype, value, traceback):
	print(f"{RED + BLD}ERROR:{RES} {value}")
	exit(1)
sys.excepthook = my_except_hook
