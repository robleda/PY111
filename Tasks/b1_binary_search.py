from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	low = 0
	high = len(arr) - 1
	result = None
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == elem:
			result = mid
			break
		elif arr[mid] > elem:
			high = mid - 1
		elif arr[mid] < elem:
			low = mid + 1

	return result
