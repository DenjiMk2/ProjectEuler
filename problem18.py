import sys
sys.setrecursionlimit(10000)
def explorer(row,col,m):
	print("row"+str(row)+"col"+str(col))
	if len(m) <= row+1:
		return m[row][col]
	else:
		forward = explorer(row+1,col,m)
		backward = explorer(row+1,col+1,m)
		return m[row][col]+max(forward,backward)
print(explorer(0,0,[list(map(int,input().split())) for i in range(int(input()))]))
