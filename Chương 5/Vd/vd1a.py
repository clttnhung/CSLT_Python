#Nhập vào 1 số nguyên n và n số nguyên, lưu trữ vào 1 list L;
# Nhập vào một số nguyên x, in lên màn hình số chỉ mục của phần tử đầu tiên có giá trị bằng x trong L
n=int(input('n='))
L=[]
print('nhap vao',n,'so nguyen:')
i=1
while i<=n: #hoac for i in range(n)
    a=int(input()) 
    L=L+[a] #hoac L.append(a)
    i=i+1
print('Nhap mot so nguyen:')
x=int(input('x='))
if x in L:
    print('So chi muc cua',x,'la',L.index(x))
else:
    print('Khong tim thay')
