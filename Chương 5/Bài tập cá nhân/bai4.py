# Nhập từ bàn phím một số nguyên n (n>0) và n số nguyên lưu vào List A:
#- Hãy đảo ngược giá trị của các phần tử trong List A và lưu vào List B. In giá trị các phần tử trong 
#List B sau khi thực hiện đảo;
#- Sắp xếp và in lên màn hình List B sau khi được sắp xếp tăng dần



n=int(input('n='))
L=[]
for i in range(1,n+1):
 a=int(input())
 L=L+[a]
M=L.copy()
L.reverse()
print(L)
M.sort()
print(M)
