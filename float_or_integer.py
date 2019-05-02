def i_or_f(arr):
	try:
		n = float(arr)
	except ValueError: return False
	return True if n is not None else False