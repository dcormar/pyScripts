def tickets(people):
	#billsNeeded = [[(x-25)/25,int((x-25)/50)] for x in people]
	twentyFives = 0
	fifties = 0
	for x in people:
		if x==25:
			twentyFives +=1
		elif x==50:
			if twentyFives == 0:
				return False
			else:
				twentyFives -=1
				fifties +=1
		elif x==100:
			if twentyFives == 0:
				return False
			elif fifties == 0 and twentyFives < 3:
				return False
			else:
				if fifties >0:
					twentyFives -=1
					fifties -=1
				else:
					twentyFives -=3
	return True

print(tickets([25, 25, 50, 50, 100]))