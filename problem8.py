import sys
target = list(map(int,list(sys.argv[1])))
targetLen = int(sys.argv[2])
ret = 0
for i in range(len(target)-targetLen+1):
	slicedtarget = target[i:i+targetLen]
	producttarget = 1
	for j in slicedtarget:
		producttarget *= j
	if producttarget > ret :
		ret = producttarget
print(ret)