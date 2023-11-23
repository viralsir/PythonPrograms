# set1={23,33,44,55}
# print(set1)
# set1.add(345)
# print(set1)
# set1.add(input("Enter no:"))
# print(set1)
# set1.remove(33)
# print(set1)
#
# print("using for each loop:")
# for element in set1:
#     print(element)

set1={1,2,3,4,5}
set2={4,5,6,7,8}

print("intersection")
#insertsection
set3=set1 & set2
set4=set1.intersection(set2)
print(set3)
print(set4)

#diff
print("difference")
set3= set1 - set2
set4= set2.difference(set1)
print(set3)
print(set4)


#union
print("union")
set3=set1 | set2
set4=set1.union(set2)
print(set3)
print(set4)

#symmetric difference
print("symmetric difference")
set3=set1 ^ set2
set4=set1.symmetric_difference(set2)
print(set3)
print(set4)

set5={3,4,3,4,4,4,4,3}

print(set5)





