def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0:
		raise ValueError
	elif n == 0:
		return 0
	elif n <= 2:
		return 1
	return fib_recursive(n - 1) + fib_recursive(n - 2)



def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0:
		raise ValueError
	elif n == 0:
		return 0
	elif n <= 2:
		return 1
	fib1 = fib2 = 1
	fib_sum = None
	for i in range(3, n + 1):
		fib_sum = fib1 + fib2
		fib1 = fib2
		fib2 = fib_sum
	return fib_sum