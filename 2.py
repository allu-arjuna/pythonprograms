n=int(input("Enter the length of Fibonacci series: "))
a=0
b=1
if(n<1):
  print('Enter a valid length')
else:
  for i in range(n):
    print(a)
    a,b=b,a+b
