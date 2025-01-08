'''
IMPORTED METHODS
'''
from icecream import ic # To substituted print function giving more information
import os
'''
EXCEPTION

Basically, the exception in python means error handler and avoids the program stop with the error. Using exceptions, it is possible to control the program flow and continue with the execution in case there is an issue like, for example, zero division or try to open a file that does not exist.

The main points here are:
    - Try: Under this function, it should be the code that makes the error.
    - except: what the program should do in case an error is found. As argument, this function uses the error or traceback name, like ZeroDivisionError or FileNotFoundError.
    - else: the rest of the code that should be execute in case there are no errors.
    - finally: What the program will execute always, independing of an exception exists or not.

    it is possible to handle different types of exceptions as follow:
'''

try:
    with open("file3.txt") as f_o:
    #with open("_42_file2.txt") as f_o:
        content = f_o.readlines()
except FileNotFoundError as fnfe:   #File does not exist. Savin data in object fnfe to get more info such as error nb
    ic(f"Error: {fnfe}")
except PermissionError:             #No permission to read the file
    print("You don't have permission to read this file.\n")
except IOError:
    print("An IO error occurred.\n") #IO error
except Exception as e:              #Some other exception
    print(f"An unexpected error occurred: {e}")
else:
    for line in content:
        ic(line)
finally:
    print("Closing the program.\n")
