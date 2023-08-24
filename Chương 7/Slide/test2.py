n=input()
m=n.find('Email:')
k=n.find('',m)
gmail = ""
if len(n)!=k+6:
 gmail=n[k+7:]
print(gmail, end="")

