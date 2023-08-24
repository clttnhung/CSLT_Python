#Viết chương trình:
# Nhập vào một chuỗi gồm các từ được phân tách bởi dấu phẩy;
# Chương trình thực hiện loại bỏ các từ trùng lắp, sau đó sắp xếp các từ theo thứ tự bảng chữ cái, phân 
#tách nhau bởi dấu phẩy rồi in kết quả ra màn hình.
M=[]
n=input()
L=n.split(',')
for i in L:
    if i not in M:
        M=M+[i]
M.sort() # sắp xếp thứ tự chuỗi
m=','.join(M)
print(m)


