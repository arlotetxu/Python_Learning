'''
IMPORTED METHODS
'''
from icecream import ic # To substituted print function giving more information
import os
'''
WORKING WITH LISTS
'''

'''
===============================UNPACKING LISTS=================================
'''
'''
Unpacked a list is possible assigning variable to its values in order
'''
list0 = [0, 1, 2, ['a', 'b']]
val1, val2, val3, val4 = list0
ic(val1, val2, val3, val4)


'''
It is possible to use the character * to unpack a list
'''
list1 = [1, 2, 3, 4]
upl1, upl2, *rest = list1
ic(list1)
ic(upl1, upl2, rest)


'''
Even it is possible unpacking when passing arguments to a function
'''
def suma(a:int, b:int, c:int) -> int:
    return (a + b + c)

list2 = [5, 6, 7]
result = suma(*list2)
ic(result)


'''
Integrating a list into another
'''
list3 = [10, 11, 12]
list4 = [*list3, 13, 14, 15]
ic(list4)
