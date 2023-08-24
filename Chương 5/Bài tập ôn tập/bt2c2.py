L=[1,2,4,5]
x=int(input("x="))
def search(L,x):
    for n in range(len(L)):
        if x==L[n]:
            return n
    return None
print(search(L,x))