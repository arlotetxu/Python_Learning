'''
IMPORTED METHODS
'''
from icecream import ic # To substituted print function giving more information
import os
'''
WORKING WITH FILES

Some examples of how to work with files in python language.
We will see how to use the open() function to read a file in different ways and how to write a file also in different ways.

﻿the open() function’s arguments and defaults:
 open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

As argument to the mode parameter, it is possible to use:
    - blank --> by default, read mode
    - 'r' -> Read mode.
    - 'w' -> Write mode. If file exists, replace its contents
    - 'a' -> Append mode. Add content at the end of the file.
    - 'b' -> Bynary mode.
    - 't' -> Text mode (default)
    - 'r+' -> Read & Write mode.
    - 'w+' -> Read & Write mode but the previous content is deleted.
    - 'a+' -> Read & Append mode.

    When you are out of the with statement, the file closes automatically, so the file object is not accesible.
'''

'''
=================================READING FILES==================================
'''
# macos:
# file_path = "/Users/arlo/Documents/Mis_Proyectos/Python/Personal_Cheatsheet/_41_file1.txt"
# linux:
file_path = "_41_file1.txt"

# Reading a file
with open(file_path) as f_o:
    '''
    Here the file is read and load entirely into memory
    '''
    content = f_o.read() # content is str type
ic(content)
ic(type(content))

f_o = open(file_path)
ic(f_o.read())
f_o.close()

'''
It is recommended the using of 'with' because in this case, python automatically
close the file once finished the 'with' block. Otherwise, the file must be close
manually as in the previous statements.
'''

# Reading line by line
with open(file_path) as f_o:
    '''
    line is str type. It is the recommended method to read a file because the file is read line by line and in that case, there won't run out of memory.
    '''
    for line in f_o:
        # ic(type(line))
        ic(line.strip())


# Adding the lines of a file to a list
with open(file_path) as f_o:
    '''
    The following case is not recommended as the file is read as a whole you can get an out of memory issue
    '''
    lines = f_o.readlines() #lines is list type
    ic(lines[0])
all_Content = ''
for line in lines:
    all_Content += line.strip()

ic(all_Content)


'''
==================================WRITING FILES=================================
'''

#macos
#file_path_2 = "/Users/arlo/Documents/Mis_Proyectos/Python/Personal_Cheatsheet/_42_file2.txt"
#linux:
file_path_2 = "_42_file2.txt"


# Simple writting
with open(file_path_2, 'w') as f_o:
    f_o.write("Adding content to the file.")


# Adding more content, but it is added to the same line.
# When the same file is open in writting mode, the previous content is deleted.
with open(file_path_2, 'w') as f_o:
    f_o.write("Adding content to the file_2.") # \n is possible to add new lines
    f_o.write("MORE CONTENT TO THE FILE.")


# Adding content without deletion. It is used the "append" mode as 'a'
with open(file_path_2, 'a') as f_o:
    f_o.write("\nAdding new lines to the file.")
