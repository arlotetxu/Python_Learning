'''
IMPORTED METHODS
'''
from icecream import ic # To substituted print function giving more information

'''
Functions are pieces of code that are usually execute more than one time or
pieces of code that makes a specific action. It is recommended use a function
for one single purpose. By this way, maintain or modify the code becomes easier
for the programmers.
'''

'''
==========================DEFINING A SIMPLE FUNCTION============================
'''

def greeting():
    ic("Hello user!.")

# Calling a function
greeting()

'''
==========================USING PARAMETERS IN FUNCION===========================
Using the type hinting, it is possible to specify what data type must be the
argument (name in our case must be a string data type) and what data type must
return the function (None in the following case as this function does not
return any data). Python, by default, doesn't check if this type hinting code is fulfiling
the data types as it is dinamic asigning language but using the module "mypy",
this issue is controlled showing a traceback when fails. To run mypy, open a
terminal and execute "mypy name_of_program.py"
'''

def greeting_par(name: str) -> None:
    ic(f"Hello, {name.title()}!.")

greeting_par("jose")


'''
=============================POSITIONAL PARAMETERS==============================
It is possible pass parameters (values) to the functions according to their
position:
'''

def greeting_par_pos(name: str, age:int) -> None:
    ic(f"{name.title()} is {age} years old!.")

# When calling the function, the first parameter corresponds to the name.
# The second parameter is the age.
greeting_par_pos("jose", 44)

# The following call will create a Attribute error.
# greeting_par_pos(44, "jose")


'''
==============================KEYWORD PARAMETERS===============================
It is also possible pass parameters (values) to the functions specifying the
name of the parameter:
'''

def greeting_par_key(name: str, age: int) -> None:
    ic(f"{name.title()} is {age} years old!.")

greeting_par_key(age = 44, name = "jose")


'''
=============================OPTIONAL PARAMETERS===============================
It is possible define a function with optional parameters. To do this, it is
only needed to assign a blank value in the definition. To add this parameter
to the function logic, you must specify its value in the function call.
'''

def user_data_opt(name: str, age: int, address: str = '') -> None:
    if address:
        print(f"User: {name.title()}\nAge: {age}\nAddress: {address}")
    else:
        print(f"User: {name.title()}\nAge: {age}\n=======================")

user_data_opt("jose", 44)
user_data_opt("jose", 44, "Madrid, Spain")


'''
===============================FUNCTION RETURNS================================
Usually, there are 2 types of functions; those that show information and those
that get data, tranform it and then return the result. To return a value, the
word "return" at the end of the function is needed with the value to return.
The value a function returns, often is used by other functions.
'''

def sum(a:int, b:int) -> int:
    return (a+b)

def mult_2(a:int) -> int:
    return (a*2)

# It is possible store the returned value of a function in a variable
returned = sum(5, 3)
ic(returned)
# Calling a functions that uses the return of other function as argument.
returned_mult = mult_2(sum(5,3))
ic(returned_mult)


'''
======================USING *ARG & **KWARGS AS PARAMETERS=======================
When the number of arguments to pass to a function is unknown, the use of the
statement *args is possible. The name args is optional (can be used whatever)
but args is commonly used. When calling the function, you can pass whatever
parameters and they are managed by the funcion as a tuple of arguments that
can be acceses as it is iterable.
'''

#------------------------------------*ARGS--------------------------------------
def check_args(*args) -> None:
    for arg in args:
        ic(arg)
    # Or it is possible use one of them if the position is known
    ic(args[3])
    ic(type(args)) # It is a tuple

check_args(1, 5, 7, "Peter", (10, 20, 30))


# If one parameter is mandatory, it is possible use the following:
def one_required(required, *args):
    print(f"{required=}")
    print(args)

one_required("Mikel", 1, 5)
#one_required() -> TypeError: one_required() missing 1 required positional argument: 'required'


#-----------------------------------**KWARGS------------------------------------
'''
In the case of **kwargs, the method is quite similar (the number of parameters
are unknown) but in this case, the parameters are keywords type. That means it
is mandatory specify the name of the parameters and their values. In this case,
the parameter is managed by the function as a dictionary.
'''

def check_kwargs(**kwargs) -> None:
    for key, value in kwargs.items():
        ic(f"Key: {key} -- Value: {value}")

check_kwargs(One= 1, Two= 2, Name= 'Frank')


#------------------------------*ARGS & **KWARGS---------------------------------
'''
But, what happens if the function needs both *args and *kwargs to do its code?
in that case, it is needed to specify which one is in the call as following:
'''
my_tuple = (1, 2, 3, 4, 5)
my_dict = {"One": 1, "Two": 2, "Name": 'Bob'}

def check_both(*args, **kwargs) -> None:
    ic(args)
    ic(kwargs)

check_both(my_tuple)
# ic| args: ((1, 2, 3, 4, 5),)
# ic| kwargs: {}
#
check_both(my_tuple, my_dict) # The funcion considers there is only 1 argument
# ic| args: ((1, 2, 3, 4, 5), {'Name': 'Bob', 'One': 1, 'Two': 2})
# ic| kwargs: {}

check_both(*my_tuple, **my_dict) # This is the right way
# ic| args: (1, 2, 3, 4, 5)
# ic| kwargs: {'Name': 'Bob', 'One': 1, 'Two': 2}
#
