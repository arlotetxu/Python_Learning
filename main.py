'''
IMPORTED METHODS
'''
from icecream import ic # To substituted print function giving more information

'''
WORKING WITH STRINGS

String data tyoes are a list os characters. The character must always be between
simple quatation marks '' or double.
'''

name = 'Arlo'
lastname = "TeTxu"
# String Methods

# Cast
value = 5
ic(type(value))
value_str = str(value)
ic(type(value_str))

# Merge 2 strings
merged = name + " " + lastname
ic(merged)

#Split
'''
By default, if you do not indicate the character to be used as separator, it is
considered the blank space as it.
The built-in function returns a list (iterable) with all the words in the string
'''
splitted = merged.split()
ic(splitted)
for word in splitted:
	ic(word)
