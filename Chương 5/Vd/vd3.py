#Tách những số nguyên tại ví trí có số chỉ mục chẵn trong L và lưu vào list M
# Xóa những phần tử tại vị trí có số chỉ mục chẵn trong L. In lên màn hình
L=[1,2,3,4,5,6,7,8,9]
#Cau a
M=[]
for i in range(len(L)): 
  if i%2==0:  # neu i la so chi muc chan
    M.append(L[i])
print("Cac phan tu co so chi muc chan: ",M)
 
#Cau b
K=[]
for i in range(len(L)):
  if i%2!=0:  #i la so chi muc le
    K.append(L[i])
L=K.copy()
print("Cac phan tu co so chi muc le: ",L)


