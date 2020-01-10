from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""

	for j in range(len(container)):
		swapped = False
		for i in range(len(container) - 1 - j):
			if container[i] > container[i + 1]:
				container[i], container[i + 1] = container[i + 1], container[i]
				swapped = True

		if not swapped:
			break



	return container
