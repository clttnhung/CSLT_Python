#Nhập 3 số thực từ bàn phím, in lên màn hình số lớn nhất và bé nhất trong 3 số trên.
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a>b:
    if a>c:
        max=a
        if b>c:
            min=c
        else:
            min=b
    else:
        max=c
        min=b
else: 
    if b>c:
        max=b
        if a>c:
            min=c
        else:
            min=b
    else:
        max=c
        min=a
print("SLN="+str(max))
print("SBN="+str(min))
