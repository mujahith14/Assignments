#Given a nested list by adding the Sublist
list= ["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sublist=["h","i","j"]
list[2][1][2].extend(sublist)
print(list)

#Find value 20 in the list and if it is present replace it with 200
list1=[5,10,15,20,25,50,20]
list1[3]=200
print(list1)

#Unpacking the given tuple
atuple=(10,20,30,40)
a,b,c,d=atuple
print(a)
print(b)
print(c)
print(d)

#Copy the element 44 and 55 from the tuple into a new tuple
tuple1=(11,22,33,44,55,66)
tuple2=tuple1[3:5]
print(tuple2)

#Renaming key "city" to "location" 
simpledict={
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"New York"
}
simpledict["Location"]=simpledict.pop("city")
print(simpledict)

#geeting the key of minimum value
sampleDict={
    'physics':82,
    'math':65,
    'history':75
}
print(min(sampleDict,key=sampleDict.get))
