L=[1,4,5,2,5,5,6]
x=int(input("x="))
def delete(L,x):
 while x in L:
  L.remove(x)
  return(L)
print(delete(L,x))