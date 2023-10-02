n=input('Enter a multi digit number')
f={}
for d in n:
    if d in f:
        f[d]+=1
    else:
        f[d]=1
print("Digit frquencies: ")
for d in f:
    print(d+" :",f[d])
