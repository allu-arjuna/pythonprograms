size = int(input("Enter the number of values to be input: "))
numbers=[]
for i in range(size):
    n = float(input("Enter a number: "))
    numbers.append(n)

mean = sum(numbers)/N
var = sum((x-mean)**2 for x in numbers)/N
sd = var**0.5
-
print('The mean of the number is: ', mean)
print('The variance of the number is: ', var)
print('The standard deviation of the number is ', sd)
