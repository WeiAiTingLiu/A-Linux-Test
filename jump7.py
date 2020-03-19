a = 1
while a < 101:
    if a // 10 == 7 or a % 7==0:
        a = a+1
        continue
    else:
        print(a)
        a = a+ 1
