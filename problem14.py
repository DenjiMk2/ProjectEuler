import sys
sys.setrecursionlimit(10000)
dict = {}
def colatLon(e):
	# print(e)
	if e in dict:
		return dict[e]
	if e == 1:
		return 1
	if e % 2 == 0 :
		temp = 1+colatLon(e//2)
		dict[e] = temp
		return temp
	else:
		temp = 1+colatLon(3*e+1)
		dict[e] = temp
		return temp
ret = 0
retI = 0
for i in range(1,1000001):
	lon = colatLon(i)
	if lon > ret :
		print(i)
		ret = lon
		retI = i
print(str(lon)+" "+str(retI))
# print(dict)