#Hàm count(L) trả về số lượng phần tử trong List L; (tương tự hàm len())
L=[1,2,3,4,5,6]
def count(L):
    k=0
    for i in L:
        k=k+1
    return k
print(count(L))