from re import M

max=0
min=10
L=input()
for i in L:
    if i.isnumeric():
        if int(i)>max:
            max=int(i)
        elif int(i)<min:
            min=int(i)
L=max,min
print(list(L))


