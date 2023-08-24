#Nhập vào 1 số nguyên n và n số nguyên, lưu trữ vào 1 list L;
# Thực hiện chèn x vào vị trí kế sau vị trí x được tìm thấy trong L, nếu x không tồn tại trong L thì chèn x vào cuối L
n=int(input('n='))
L=[]
print('nhap vao',n,'so nguyen:')
for i in range(n):
    a=int(input()) 
    L=L+[a]  
print('Nhap mot so nguyen:')
x=int(input('x='))
if x in L:
    i=L.index(x)
    L=L[:i]+[x]+L[i:]
else:
    L=L+[x]
print(L)