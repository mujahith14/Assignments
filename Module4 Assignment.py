#Dicount
quantity=int(input("What is the Quantity: "))
totalamount=(quantity)*100
if totalamount>1000:
    discount=totalamount-totalamount/10
    print("Price After Discount: ",discount)
else:
    print("Price Without Discount: ",totalamount)

#Grading System
mark=int(input("Enter the Mark: "))
if mark<=25:
    print("GRADE F")
elif mark<45:
    print("GRADE E")
elif mark<50:
    print("GRADE D")
elif mark<60:
    print("GRADE C")    
elif mark<80:
    print("GRADE B")
else:
    print("GRADE A")


#Finding Oldest and Youngest
age1=int(input("Age of 1st person: "))
age2=int(input("Age of 2nd person: "))
age3=int(input("Age of 3rd person: "))

if age1>age2 and age1>age2:
    print("1st person is older")
elif age2>age1 and age2>age3:
    print("2nd person is older")
elif age3>age1 and age3>age2: 
    print("3rd person is older")
   
if age1<age2 and age1<age3:
    print("1st person is younger")
elif age2<age1 and age2<age3:
    print("2nd person is younger")    
elif age3<age1 and age3<age2:
    print("3rd person is younger")

#Using Range Making Odd and Even List
even=[]
odd=[]
for i in range(1,101):
    if i % 2 == 0:
       even.append(i) 
for i in range(1,101):
    if i % 2 != 0:
        odd.append(i)
print("Even Numbers: ",even)
print("Odd Numbbers: ",odd)

#form the two list obtained in the previous question, make 
#new lists containing only numbers which are divisible
#by 4,6,8,10,3,5,7,9 
obtainedlist= even + odd
by4=[]
by6=[]
by8=[]
by10=[]
by3=[]
by5=[]
by7=[]
by9=[]
for i in obtainedlist:
   if i %4==0:
       by4.append(i)
   if i %6==0:
       by6.append(i)
   if i %8==0:
       by8.append(i)
   if i %10==0:
       by10.append(i)
   if i %3==0:
       by3.append(i)
   if i %5==0:
       by5.append(i)
   if i %7==0:
       by7.append(i)
   if i %9==0:
       by9.append(i)            
print("Divide by 4: ",by4)
print("Divide by 6: ",by6)
print("Divide by 8: ",by8)
print("Divide by 10: ",by10)
print("Divide by 3: ",by3)
print("Divide by 5: ",by5)
print("Divide by 7: ",by7)
print("Divide by 9: ",by9)



