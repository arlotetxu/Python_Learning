'''
IMPORTED METHODS
'''
from icecream import ic # To substituted print function giving more information

'''
=============================WORKING WITH STRINGS==============================

String data types are a list of characters. The character must always be between
simple quotation marks '' or double.
'''

name = 'arlo'
lastname = "TeTxu"

'''
STRING METHODS
'capitalize',
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
'translate', 'upper', 'zfill']
'''

# Cast
value = 5
ic(type(value))
value_str = str(value)
ic(type(value_str))


# capitalize -> Prints the first letter of the string word in uppercase
ic(name.capitalize())


# upper -> Prints the string in uppercase
ic(name.upper())


#lower --> Prints the string in lowercase
ic(lastname.lower())


# strip -> removes the whitespaces at the beginning and at the end of a string
full_Name = "Arlo TeTxu    "
ic(full_Name.strip())


# rstrip / lstrip -> removes the white spaces from the right or from the left
ic(full_Name.rstrip())


# Merge 2 strings
ic(name + " " + lastname)


#join
''''
join a list of words. Carefull, the function only accepts one argument
being usually a list of words. The first argument is the character used to
join the words.
'''
ic(' // '.join([name, lastname]))


#split
'''
By default, if you do not indicate the character to be used as separator, it is
considered the blank space as it.
The built-in function returns a list (iterable) with all the words in the string
'''
string = "This is a test for split function"
ic(string.split())


# Slicing a string
ic(string[0:5])
ic(string[:])
ic(string[1:])
ic(string[5:-9])
ic(string[::-1]) #String reverse
