#Viết chương trình nhập vào một số nguyên n (n>0) và n số nguyên lưu vào List L. 
#Thực hiện loại bỏ những phần tử có giá trị trùng nhau và lưu tập mới vào List M. In 
#lên màn hình các phần tử trong M

n=int(input('n='))
L=[]
M=[]
for i in range(0,n):
 a=int(input())
 L=L+[a]
 if L[i] not in M:
    M=M+[a]
for i in M:
    if i==M[-1]:
        print(i,end='')
    else:
        print(i,end=' ')   
