#Giai phuong trinh bac nhat: ax+b=0
a=int(input('a='))
b=int(input('b='))
if a==0:
    if b==0:
        print('Phuong trinh co vo so nghiem!!!')
    else:
        print('Phuong trinh co nghiem!!!')
else:
    print('Phuong trinh co nghiem x=',(-b/a))
    