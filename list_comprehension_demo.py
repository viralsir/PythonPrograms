list1=[x for x in range(5)]
list2=[x for x in range(5,15)]
list3=[x for x in range(0,21,2)]
maths_marks=[23,33,44,54,3,44,66,77]
sci_marks=[34,44,55,66,44,43,45,66]
maths_pass_mark=[x for x in maths_marks if x>=35]
stringlist=[x for x in "Hello How are you " if x.islower()==True]

print(list1)
print(list2)
print(list3)
print(maths_pass_mark)
print(stringlist)