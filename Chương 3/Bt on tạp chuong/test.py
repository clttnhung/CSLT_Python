c = 't'
while c == 't' or c == 'T':
    a = float(input('Nhap A: '))
    b = float(input('Nhap B: '))
    ch = input('Toan tu: ')
    if ch == '+':
        print('%.2f + %.2f = %.2f' %(a, b, a + b))
    elif ch == '-':
        print('%.2f - %.2f = %.2f' %(a, b, a - b))
    elif ch == '*':
        print('%.2f * %.2f = %.2f' %(a, b, a * b))
    elif ch == '/':
        print('%.2f / %.2f = %.2f' %(a, b, a / b))
    else:
        print('%s khong phai la toan tu!!!' %(ch))
    c = input('Nhap t||T de tiep tuc: ')


          
