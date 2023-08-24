
def Input():
    n=int(input("n="))
    L=[]
    for i in range (n):
        a=int(input(""))
        L=L+[a]
    return L
def Search(L):
    max=L[0]
    min=L[0]
    for i in range(len(L)):
        if L[i]>max:
            max=L[i]
        elif L[i]<min:
            min=L[i]
    return max, min
def Output(max,min):
    print(min,end=" ")
    print(max)

L=Input()
min,max=Search(L)
Output(max,min)