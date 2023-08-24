#Nhập vào 1 số nguyên n và n số nguyên, lưu trữ vào 1 list L;
# Nhập vào một số nguyên x, in lên màn hình số chỉ mục của tất cả các phần tử đầu giá trị bằng x trong L
n=int(input('n='))
L=[]
print('nhap vao',n,'so nguyen:')
for i in range(n):
    a=int(input()) 
    L=L+[a]  
print('Nhap mot so nguyen:')
x=int(input('x='))
for i in range(n):
    if L[i]==x:
        print(i)