#Nhập vào 3 số thực dương a, b và c, kiểm tra 3 số trên có lập thành 3 cạnh của một tam giác hay
#không. Nếu có thì hãy in lên màn hình diện tích của tam giác đó, còn không thì in thông báo: “Khong
#hop le”
#Biết rằng:
#- Điều kiện cần và đủ để a,b và c lập thành 3 cạnh của tam giác là: (a+b)>c và (a+c)>b và (b+c)>a
#- Diện tích tam giác = √(𝑝 ∗ (𝑝 − 𝑎) ∗ (𝑝 − 𝑏) ∗ (𝑝 − 𝑐))
#Với p=(a+b+c)/2

import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
p=((a+b+c)/2)
if a+b>c and a+c>b and b+c>a:
    print('Dien tich:'+str(round(math.sqrt(p*(p-a)*(p-b)*(p-c)),3)))
else:
    print('Khong hop le')
