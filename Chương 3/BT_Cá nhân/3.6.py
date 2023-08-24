#Nhập vào 3 số thực a, b và c (a,b,c>0), kiểm tra 3 số trên có lập thành 3 cạnh của một tam giác hay
#không.
#- Nếu không phải thì thông báo: “Khong hop le”
#- Còn lại thì cho biết tam giác đó thuộc loại tam giác gì: “Tam giac deu”, “Tam giac vuong”, “Tam
#giac loai khac”
#Biết rằng:
#- 3 số thực dương tạo thành 3 cạnh của một tam giác nếu: (a + b > c) và (a + c > b) và (b + c > a) và (a
#> 0) và (b > 0) và (c > 0) ;
#- Là tam giác vuông nếu: (a*a = b * b + c * c) hoặc (b * b = a * a + c * c) hoặc (c * c = a * a + b * b);
#- Là tam giác đều nếu: (a = b) và (b = c) và (c = a);
a=float(input())
b=float(input())
c=float(input())
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print('Tam giac vuong')
    elif a==b and b==c and c==a:
        print('Tam giac deu')
    else:
        print('Tam giac loai khac')
else: 
    print('Khong hop le')
