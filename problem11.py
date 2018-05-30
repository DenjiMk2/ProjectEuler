from functools import reduce
board_size = 20
board = []
board = [list(map(int,input().split())) for i in range(board_size)]
board.insert(0,[-1 for i in range(board_size)])
board.append([-1 for i in range(board_size)])
for i in range(len(board)):
	board[i].append(-1)
	board[i].insert(0,-1)
#番兵-1を周囲に配置したboard生成完了
ret = 0
#全ポイントから下に4つ
for i in range(len(board)):
	for j in range(len(board[i])):
		#print(i," ",j)
		target = []
		for k in range(4):
			#print("k"+str(i+k)+" "+str(j))
			if board[i+k][j] == -1:
				break
			target.append(board[i+k][j])
		if len(target) == 4:
			red = reduce(lambda x, y: x * y, target)
			if red >= ret:
				ret = red
#全ポイントから右に4つ
for i in range(len(board)):
	for j in range(len(board[i])):
		#print(i," ",j)
		target = []
		for k in range(4):
			#print("k"+str(i+k)+" "+str(j))
			if board[i][j+k] == -1:
				break
			target.append(board[i][j+k])
		if len(target) == 4:
			red = reduce(lambda x, y: x * y, target)
			if red >= ret:
				ret = red
#全ポイントから右下に4つ
for i in range(len(board)):
	for j in range(len(board[i])):
		#print(i," ",j)
		target = []
		for k in range(4):
			#print("k"+str(i+k)+" "+str(j))
			if board[i+k][j+k] == -1:
				break
			target.append(board[i+k][j+k])
		if len(target) == 4:
			red = reduce(lambda x, y: x * y, target)
			if red >= ret:
				ret = red
#全ポイントから左下に4つ
for i in range(len(board)):
	for j in range(len(board[i])):
		#print(i," ",j)
		target = []
		for k in range(4):
			#print("k"+str(i+k)+" "+str(j))
			if board[i+k][j-k] == -1:
				break
			target.append(board[i+k][j-k])
		if len(target) == 4:
			red = reduce(lambda x, y: x * y, target)
			if red >= ret:
				ret = red


print(ret)
