
tuple1=(12,34,44,54,23)

print(tuple1)
print(tuple1[0])
print(tuple1[-1])
print(tuple1[0:3])

# group methods for tuple
print("no of elements :",len(tuple1))
print("maximum element :",max(tuple1))
print("minimum element :",min(tuple1))
print("total :",sum(tuple1))

#tuple is immutable so append,remove , update  are not supported.
#tuple1[0]=23

for element in tuple1:
    print(element)

#tuple2=23,33,44,"vimal",344.33
#print(tuple2)

tuple2=((34,444),(1,"vimal"),(3,"viren"))

print(tuple2)
print(tuple2[1])





