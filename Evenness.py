def iq_test(numbers):
	elements = [int(x)%2 for x in numbers.split(" ")]
	evenness = 0
	if sorted(elements[0:3])[0:2] == [0, 0]:
		evenness = 1
	return elements.index(evenness)+1



print(iq_test("2 4 7 8 10"))
