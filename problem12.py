import sys
import collections
import functools
def divisor(a):
	li = []
	pointer = 2
	while pointer <= a:
		if a%pointer == 0:
			li.append(pointer)
			#print(li)
			a = a/pointer
			pointer = 2
		else:
			pointer += 1
	return functools.reduce(lambda x, y: x * (y+1), collections.Counter(li).values(),1)

for i in range(1,1000000):
	l = int(divisor(sum(list(range(i+1)))))
	print("i"+str(i)+"l"+str(l)+"sum"+str(sum(list(range(i+1)))))
	if l >= int(sys.argv[1]):
		print("success:"+str(sum(list(range(i+1)))))
		break