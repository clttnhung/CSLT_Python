def spam(divideby):
    try:
        result=42/divideby
    except:
        print('sorry! You are dividing by zezo')
    else:
        print('Yeah! Your answer is:',result)

print(spam(1))
print(spam(0))
        
    