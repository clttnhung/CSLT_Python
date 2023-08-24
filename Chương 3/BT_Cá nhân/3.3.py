#Viết chương trình sử dụng cấu trúc if thực hiện các yêu cầu sau:
#- Nhập hai số thực x, y; và một ký tự ch
#- Nếu ch là một trong các ký tự: +, -, * hoặc / thì thực hiện phép toán đó
#với x và y; nếu không thì thông báo “Khong hop le”;
#- Nếu thực hiện phép chia và y=0 thì thông báo “Khong hop le”.
#Ví dụ: Nhập x=5, y=10 và ch là ký tự: + (dấu cộng), chương trình nhập xuất
#theo mẫu bên. (Kết quả làm tròn đến 1 chữ số lẻ)

x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')
if ch=='+':
    print((str(x)+'+'+str(y)+'='+str((round((x+y),1)))))
elif ch=='-':
    print((str(x)+'-'+str(y)+'='+str((round((x-y),1)))))
elif ch=='*':
    print((str(x)+'*'+str(y)+'='+str((round((x*y),1)))))
elif ch=='/':
    if y!=0:
      print((str(x)+'/'+str(y)+'='+str((round((x/y),1)))))
    else:
        print('Khong hop le')
else:
    print('Khong hop le')
