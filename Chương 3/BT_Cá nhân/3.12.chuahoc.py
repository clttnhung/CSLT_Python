


while True:
    n = str(input('Nhap 1 so n nam trong khoang tu 1 den 9999: '))
    if len(n) > 4:
        print('1 den 9999 co ma!!!')
    else:
        print('OK, chuyen qua dang chu la: ', end='')
        break
mahoa = str('ABCDEFGHKL')
for i in n:
    print(mahoa[int(i)], end='')