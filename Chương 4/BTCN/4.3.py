#.Viết chương trình giải và biện luận phương trình bậc hai: ax2 + bx + c = 0. Trong đó a,b và c
#(a,c,b <> 0) được nhập vào từ bàn phím.
#Yêu cầu xây dựng các hàm sau:
#- Hàm nhap(),thực hiện việc nhập vào 3 số a,b và c;
#- Hàm giaipt(a,b,c),thực hiện giải và biện luận phương trình bậc hai với các tham số a, b, c
#đầu vào.
#- Hàm inkq(x1,x2): in kết quả là nghiệm của phương trình được in lên màn hình.
from cmath import e
from this import d

import math
def nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def giaipt(a,b,c):

    global d
    d=int(b*b-4*a*c)
    try:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
    except:
     print("Phuong trinh vo nghiem")
     x1=x2=None
    else: 
        if d==0:
         print('Phuong trinh co nghiem kep')
        if d>0:
         print('Phuong trinh co hai nghiem')
    return x1,x2
def inkq(x1,x2):
    if d==0:
        print('x1=x2='+str(x1))
    if d>0:
        print('x1='+str(x1))
        print('x2='+str(x2))
a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)
