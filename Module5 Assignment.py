
#Calculate a power of a number rised to other
def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
a=int(input("base: "))
b=int(input("exponent: "))
print(power(a,b))


#Perfect numbers between 1 and 1000
import math
def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    return list(set(divs))
def is_perfect_number(n):
    return n == sum(divisors(n))
res = []
for i in range(2,1001):
    if is_perfect_number(i):
        res.append(i)

print("Perfectnumbers between 1 and 1000: ",res)




#Recursuve function to calculate the sum of numbers from 0 to 10
def sum(n):
    if n==1:
      return 1
    else:
        return n+sum(n-1)

print("Sum of Numbers from 0 to 10: ",sum(10))







