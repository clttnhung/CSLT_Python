#Viết chương trình:
#- Cho phép nhập vào một chuỗi ký tự bất kỳ;
#- Chương trình thực hiện đếm có bao nhiêu chữ cái in hoa, chữ cái in thường, chữ số và ký tự khác (bao 
#gồm ký tự trắng) xuất hiện trong chuỗi trên; 
#- In kết quả lên màn hình.
def demxau(L):
    dem1=0  #Dem so chu hoa
    dem2=0  #Dem so chu thuong
    dem3=0 #Dem chu so
    dem4=0 #khac
    for i in L:
        if i.isupper():
            dem1=dem1+1
        elif i.islower():
            dem2=dem2+1
        elif i.isalnum():
            dem3=dem3+1
        else:
            dem4=dem4+1
    return dem1, dem2, dem3, dem4
L=input()
dem1,dem2,dem3,dem4=demxau(L)
print('In hoa:',dem1)
print('In thuong:',dem2)
print('Chu so:',dem3)
print('Khac:',dem4)
