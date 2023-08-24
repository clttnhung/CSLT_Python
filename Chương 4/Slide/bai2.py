def Nhap():
    a=float(input('a='))
    b=float(input('b='))
    c=float(input('c='))
    d=float(input('d='))
    return a,b,c,d
def Tinh(a,b,c,d):
    x=a+b+c+d
    y=(a+b+c+d)/4
    return x,y
def InKQ(x,y):
    print('Tong=',x,sep='')
    print('Trung binh cong=',y,sep='')
a,b,c,d=Nhap()
x,y=Tinh(a,b,c,d)
InKQ(x,y)
