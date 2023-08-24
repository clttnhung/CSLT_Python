#Viết chương trình để xóa tát cả các ký tự trắng để trong một chuỗi đã chọn
#  input:nhập vào một chuỗi ký tự 
# ouput: in lên màn hình chuỗi kí tự đã được xóa các khoảng trống 
# input:Py t ho n 
# Ouput:Python

a=input()
a=''.join(a.split())
print(a)