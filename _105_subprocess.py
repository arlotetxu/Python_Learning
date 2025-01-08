import subprocess
from icecream import ic


'''
===================EXECUTING THE LS SHELL COMMAND IN PYTHON====================
'''
subprocess.run(['ls', '-l'], shell=False)
print("\n===============================================\n")
#shell = True will execute the command whithin the shell terminal
#subprocess.run(['ls -l'], shell=True)

#To get the output:
output = subprocess.run(['ls -l'], shell=True, capture_output=True)
# ﻿output is a CompletedProcess class instance
ic(output)
ic(output.returncode)
ic(output.stdout)
ic(output.stderr)
