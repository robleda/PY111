"""
Taylor series
"""
from typing import Union
import math


def ex(x: Union[int, float]) -> float:
	"""
	Calculate value of e^x with Taylor series

	:param x: x value
	:return: e^x value
	"""
	result = 0
	for i in range(10):
		taylor = (x ** i) / math.factorial(i) # можно для оптимизации домножать на результат предыдущего знаменателя...
		result += taylor
	print(x)
	return result


def sinx(x: Union[int, float]) -> float:
	"""
	Calculate sin(x) with Taylor series

	:param x: x value
	:return: sin(x) value
	"""

	result = 0
	for i in range(10):
		taylor2 = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
		result += taylor2
	print(x)
	return result
