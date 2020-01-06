"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	mi = float('inf')
	ind: int = 0
	for i, val in enumerate(arr):
		if val < mi:
			mi = val
			ind = i
	return ind
