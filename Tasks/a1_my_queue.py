"""
My little Queue
"""
from typing import Any

q = []
def enqueue(elem: Any) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	q.append(elem)

	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	if len(q) != 0:
		return q.pop(0)
	else:
		return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""

	return q[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	q.clear()
	return None
