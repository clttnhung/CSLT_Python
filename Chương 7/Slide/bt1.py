#Viết chương trình nhập vào một xâu ký tự st1
#Nhập vào 1 xâu st2, kiểm tra nếu st2 xuất hiện trong xâu st1 thì yêu cầu nhập lại xâu khác, còn lại thì dừng lại.

n=int(input('n='))
st1=[]
for i in range(1,n+1):
 a=int(input())
 st1=st1+[a]
st2=[]
for i in range(1,n+1):
 b=int(input())
 st2=st2+[b]
while st2 in st1:
    print('Nhap lai xau khac:')
    st2=[]
    for i in range(1,n+1):
     c=int(input())
     st2=st2+[c]



