"""
My little Stack
"""

from typing import Any

stack = []

def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global stack
	stack.append(elem)


def pop() -> Any:
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	if len(stack) > 0:
		a = stack.pop()
		return a

# либо проверка на исключение, либо одно из двух

def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	b = stack[-1 - ind]
	return b


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	stack.clear()
