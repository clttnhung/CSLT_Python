#Viết chương trình nhập vào một xâu str và một ký tự ch, in lên màn
#hình số lượng ký tự ch xuất hiện trong xâu str (không phân biệt chữ hoa và chữ thường).
#Ví dụ:
#str=Learn PYTHON Programming
#ch=n
#Number of character n is: 3
k=0
str=input('str=').upper()
ch=input('ch=').upper()
for i in str:
    if ch==i:
     k=k+1
print('Number of character n is:',k)

