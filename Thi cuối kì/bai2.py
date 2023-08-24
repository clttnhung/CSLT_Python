n=input()
L=[]+[n]
if int(n)>=0:
 tong=int(n)
else:
    tong=0
dem=1
while n!='Q':
    n=input()
    if n.isdecimal():
        if int(n)>=0:
            tong=tong+int(n)
print(tong)