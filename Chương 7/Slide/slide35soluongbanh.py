Tenmon=[]
Soluong=[]
for i in range(4):
    ten=input()
    Tenmon.append(ten)
    sl=input()
    Soluong.append(sl)
for i in range(4):
    print(Tenmon[i].ljust(20,'.'),end='')
    print(Soluong[i].rjust(10))