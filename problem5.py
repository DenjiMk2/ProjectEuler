ret = 1
checkList = list(range(1,21))
while not(all(ret%e==0 for e in checkList)):
	#print(ret)
	ret+=1
print(ret)