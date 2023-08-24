n=input()
x=input()
L=n.split()
if x in L:
    for i in range(len(L)):
     if x==L[i]:
        print(i+1)
else:
    print(0)
    