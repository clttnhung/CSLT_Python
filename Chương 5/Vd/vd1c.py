#Nhập vào 1 số nguyên n và n số nguyên, lưu trữ vào 1 list L;
# Nhập vào một số nguyên i, thực hiện chèn x vào L tại vị trí có số chỉ mục i
n=int(input('n='))
L=[]
print('nhap vao',n,'so nguyen:')
for i in range(n):
    a=int(input()) 
    L=L+[a]  
print('Nhap mot so nguyen:')
i=int(input('i='))
x=int(input('x'))
L.insert(i,x)
print(L)
