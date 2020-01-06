import Tasks.a0_my_stack as bracket_stack


def check_brackets(brackets_row: str) -> bool:
    """
	Check whether input string is a valid bracket sequence
	Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
    for i in brackets_row:
        if i == "(":
            bracket_stack.push(i)
        elif i == ")":
            if not bracket_stack.stack:
                return False
            else:
                bracket_stack.pop()
        else:
            continue
    if not bracket_stack.stack:
        res = True
    else:
        res = False
    bracket_stack.clear()
    return res
