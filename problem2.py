befor1 = 2
befor2 = 1
curent = 0
ret = 2
while curent < 4000000:
    curent = befor1+befor2
    if curent % 2 ==0:
        ret += curent
    befor2 = befor1
    befor1 = curent
print(ret)
