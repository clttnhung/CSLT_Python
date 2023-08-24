#ktra so nguyen to
def Nhap():
    n=int(input('n='))
    return n
def LaSNT(x):
    for i in range(2,x):
        if x%1==0:
            return False
    return True
def InKQ(n):
    if LaSNT(n):
      print(n,'la SNT')
    else:
        print(n,'khong la SNT')

n=Nhap()
InKQ(n)