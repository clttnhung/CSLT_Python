#Nhập một số nguyên n (0<=n<=9999) từ bàn phím. In lên màn hình giá trị đã được mã hóa theo quy
#tắc sau:
# Các chữ số nằm trong số nguyên n được mã hóa thành chữ cái;
# Các chữ số được mã hóa theo quy tắc sau:
#0 -> A; 1 -> B; 2 -> C; 3 -> D; 4 -> E; 5 -> F; 6 -> G; 7 -> H; 8 -> K; 9 -> L
n=int(input())
d=len(str(n))
for i in range(d-1,-1,-1):
    a=n//(10**i)
    n=n%(10**i)
    if a==0:
        print('A',end='')
    elif a==1:
        print('B',end='')
    elif a==2:
        print('C',end='')
    elif a==3:
        print('D',end='')
    elif a==4:
        print('E',end='')
    elif a==5:
        print('F',end='')
    elif a==6:
        print('G',end='')
    elif a==7:
        print('H',end='')
    elif a==8:
        print('K',end='')
    elif a==9:
        print('L',end='')
  