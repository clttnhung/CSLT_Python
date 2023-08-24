#Nhập một số nguyên n (0<=n<=9999) từ bàn phím. In lên màn hình giá trị đã được mã hóa theo quy
#tắc sau:
# Các chữ số nằm trong số nguyên n được mã hóa thành chữ cái;
# Các chữ số được mã hóa theo quy tắc sau:
#0 -> A; 1 -> B; 2 -> C; 3 -> D; 4 -> E; 5 -> F; 6 -> G; 7 -> H; 8 -> K; 9 -> L
while True:
    n = int(input('Nhap 1 so n nam trong khoang tu 1 den 9999: '))
    if n > 9999:
        print('1 den 9999 co ma!!!')
    else:
        print('OK, chuyen qua dang chu la: ', end='')
        break
k = int()
while n > 0:
    k = (k + int(n % 10))*10
    n = (n - n%10)/10 
k = int(k/10)
while k > 0:
    l = k - (int(k/10)) *10
    k = (k - l)/10
    if l == 0:
        print('A', end='')
    elif l == 1:
        print('B', end='')
    elif l == 2:
        print('C', end='')
    elif l == 3:
        print('D', end='')
    elif l == 4:
        print('E', end='')
    elif l == 5:
        print('F', end='')
    elif l == 6:
        print('G', end='')
    elif l == 7:
        print('H', end='')
    elif l == 8:
        print('K', end='')
    elif l == 9:
        print('L', end='')