#Nhập chuỗi bất kì, đếm số chữ cái và chữ số

def DemXau(st):
    dem1=0  #Dem so chu cai
    dem2=0  #Dem so chu so
    for x in st:
        if x.isalpha():
            dem1=dem1+1
        elif x.isnumeric():
            dem2=dem2+1
    return dem1, dem2
 
st=input()
dem1,dem2=DemXau(st)
print("Chu cai:",dem1)
print("Chu so:",dem2)

