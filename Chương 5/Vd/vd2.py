# Cho tap L gom 7 so nguyen
#Nhap mot số nguyên x, tìm và xóa tất cả các phần tử có giá trị bằng x trong L
L=[1,2,5,3,5,5] 
print('Nhap mot so nguyen:')
x=int(input('x='))
for i in L:
      L.remove(x)
print(L)