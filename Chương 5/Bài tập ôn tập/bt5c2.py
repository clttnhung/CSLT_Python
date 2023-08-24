L=[1,2,4,1,2,4]
x=int(input('x='))
y=int(input('y='))
def update(L,x,y):
    for i in range(len(L)):
        if x==L[i]:
            L=L[:i]+[y]+L[i+1:]
print(update(L,x,y))    