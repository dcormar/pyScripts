def sort_array (source_array):
	odds = list(filter(lambda x: x%2 != 0 , source_array))
	odds.sort(reverse=True)
	return [x if x%2 == 0 else odds.pop() for x in source_array]



print sort_array([5, 3, 2, 8, 1, 4])