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
	while low < high:
		mid = (low + high) // 2
		if elem > arr[mid]:
			low = mid + 1
		else:
			high = mid
	if arr[high] == elem:
		return high
	else:
		return None




