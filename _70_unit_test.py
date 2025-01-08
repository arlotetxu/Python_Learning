'''
IMPORTED METHODS
'''
from _71_unit_test_source import addition
from _72_unit_test_source import calculator
import unittest
from hypothesis import given, strategies as st
from icecream import ic # To substituted print function giving more information

'''
There are some different ways to test your code. One of these methods is the
unit test. They are unitary test to check if the output of your code is what you expect depending on the input. To do so, it is needed to import the function that is going to be assesed and the module "unittest".
'''

'''
======================CHECKING A SIMPLE FUNCTION============================
We will check the addittion function
'''

class AddittionTestCase(unittest.TestCase):
    '''To test the addittion function'''

    def test_addition(self):
        result = addition(12.0, 15)
        self.assertEqual(result, 27)

    #The following test will fail
    def test_addition_2(self):
        result = addition("a", "b")
        self.assertEqual(result, "ac")


'''
===============================CHECKING A CLASS================================
We will check the methods in a class
'''

class   CalculatorTestCase(unittest.TestCase):
    '''To test all the methods of the class defined in _72_unit_test_source.py.
    To check each module, it is needed to create a instance to the class
    in it (comented with doble ##). To avoid do this, it is possible to
    define a new method (SetUp()) in the test class (CalculatorTestCase) to create all the objects to be used in the rest of the modules. This method should be define the first so when pyhton finds this method, before
    execute each of them, this special method is called.
    BEAR IN MIND the SetUp() method belongs to unittest.TestCase module'''

    def setUp(self) -> None:
        self.instc = calculator(5, 3)

    def testAdd(self):
        #creating the instance of the class to be tested
        ##suma = calculator(5, 3)
        ##result = suma.sum()
        result = self.instc.sum()
        ##ic(type(suma))
        ic(result)
        self.assertEqual(result, 8)

    def testRes(self):
        #Ready to fail
        ##rest = calculator(5, 3)
        ##result = rest.rem()
        result = self.instc.rem()
        self.assertLess(result, 1)

    def testMult(self):
        mult = calculator(5, 3)
        result = mult.mult()
        self.assertEqual(result, 15)

    def testDiv(self):
        div = calculator(5, 3)
        result = div.div()
        self.assertGreater(result, 0)

'''
==============================ALTERNATIVE MODULE===============================
There is the "hypothesis" module to perform similar tests to a function
'''

def adding(num1: int, num2:int) -> int:
    add = calculator(num1, num2)
    res = add.sum()
    return res

@given(st.integers(min_value=10), st.integers(min_value=10))
def test_adding(a:int, b:int):
    result = adding(a, b)
    assert result < 20  #Forcing the fail


if __name__ == '__main__':
    '''Execute one each time to see the results'''
    unittest.main()
    #test_adding()
