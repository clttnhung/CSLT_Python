#Nhập từ bàn phím một số nguyên n, trong đó n>=1 và n<=50.
#Nếu n không thuộc miền trên thì yêu cầu nhập lại.

n=int(input('n='))
while n<1 or n>50:
    print('Khong hop le!!!\nMoi nhap lai!!!')
    n=int(input('n='))
