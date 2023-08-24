


n=input())
dem=0
tong=0
for i in range(1,n+1):
    a=input()
    if a.isnumeric():
        dem=dem+1
        tong=tong+int(a)
if dem!=0:
 tbc=float(tong/dem)
 print(tbc)
else:
    print(0)