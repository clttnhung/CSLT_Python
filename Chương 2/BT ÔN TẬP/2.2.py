#Giá bán=Giá niêm yết-Chiết khấu+VAT
#VAT=(Giá niêm yết-Chiết khấu)*0.01
a=int(input('Nhap Gia niem yet: '))
b=int(input('Nhap Chiet khau: '))
VAT=(a-b)*0.01
c=a-b+VAT
print('Gia ban:',c)