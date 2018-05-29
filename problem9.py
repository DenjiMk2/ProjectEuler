import itertools
for i in itertools.combinations_with_replacement('123',997):
    a = i.count('1')+1
    b = i.count('2')+1
    c = i.count('3')+1
    if a**2+b**2==c**2:
        print(a," ",b," ",c)
        print(a*b*c)
        break
