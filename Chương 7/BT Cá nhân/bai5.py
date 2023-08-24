#Viết chương trình:
#- Nhập vào một chuỗi gồm các số nguyên, mỗi số cách nhau bởi một dấu cách; và một số nguyên X;
#- Chương trình thực hiện tìm X trong dãy số trên, in lên màn hình thứ tự xuất hiện của X nếu có. Nếu 
#không tìm thấy thì trả về 0

n=input()
x=input()
L=n.split()
if x in L:
    for i in range(len(L)):
     if x==L[i]:
      print(i+1)
else:
    print(0)