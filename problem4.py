def isUro(s):
    in1 = str(s)
    rev1 = in1[::-1]
    return in1 == rev1
ret = 0
for i in range(1000):
    for j in range(1000):
        if isUro(i*j):
            if i*j > ret:
                ret = i*j
print(ret)
