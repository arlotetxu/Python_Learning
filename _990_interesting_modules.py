'''
================= UNIT TEST =================
'''
import unittest     #To perform unit tests
from hypothesis import given, strategies as st # To perform test
'''
#Probando decorador
@given(st.integers(min_value=0), st.integers(min_value=0), st.integers(min_value=0), st.integers(min_value=0), st.integers(min_value=0))
def test_sumaMonedas(a: int, b: int, c: int, d: int, e: int):
    resultado = sumaMonedas(a, b, c, d, e)
    assert resultado >= 0

test_sumaMonedas()
'''

'''
================= ARITMETHICS =================
'''
import math

'''
================= DETAIL PRINT =================
'''
from icecream import ic

'''
================= DATES & TIME =================
'''
from datetime import datetime #to work with dates and time
