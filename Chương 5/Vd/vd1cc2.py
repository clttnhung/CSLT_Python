#khong dung insert
n=int(input('n='))
L=[]
print('nhap vao',n,'so nguyen:')
for i in range(n):
    a=int(input()) 
    L=L+[a]  
print('Nhap mot so nguyen:')
i=int(input('i='))
x=int(input('x='))
L=L[:i]+[x]+L[i:]
print('sau khi chen L:',L)
