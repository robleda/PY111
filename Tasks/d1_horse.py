def calculate_paths(shape: (int, int), point: (int, int)) -> int:
	"""
	Given field with size rows*cols count available paths from (0, 0) to point

	:param shape: tuple of rows and cols (each from 1 to rows/cols)
	:param point: desired point for horse
	:return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
	"""
	board = [[i for i in range(shape[1])] for x in range(shape[0] - 1)]

	print(shape, point)
	return 0



n = 11
# обратный порядок пересчета
fib = [0 for i in range(15)]
fib[1] = 1  # start value
for i in range(1, n):
    fib[i + 1] += fib[i]  # обновление состояния i + 1
    fib[i + 2] += fib[i]  # обновление состояния i + 2
# print(fib[n])