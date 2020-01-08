from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	def my_binary_search(elem, arr, low, high):
		mid = (low + high) // 2
		if elem == arr[mid]:
			return mid
		elif elem < arr[mid]:
			return my_binary_search(elem, arr, low, mid - 1)
		else:
			return my_binary_search(elem, arr, mid + 1, len(arr) - 1)
	if elem not in arr:
		return None
	else:
		return my_binary_search(elem, arr, 0, len(arr) - 1)
