'''
list : is a shared name of multiple memory location.
[]
no=[23,3,44]
'''
no=[23,33,44,34,54,65,77,33,33]

print(no)
print(no[0])
print(no[-1])
print(no[0:4])
print(no[0:6:2])
print(no[2:])
print(no[-3:])

#list is mutable (can update,delete,insert)
no[1]=234
print(no)

#inbuilt function of list
#add value to the list
no.append(2356)
print(no)
no.insert(1,3455)
print(no)

#remove or delete the element
#delete element by value
no.remove(44)
print(no)
#delete the element by index
no.pop(2)
print(no)

no.reverse()
print(no)
no.sort(reverse=True)
print(no)
print("no of times 33 in the list : ",no.count(33))

#group function
print(" no of elements :",len(no))
print(" max element of list :",max(no))
print(" min element of list :",min(no))
print(" total of all element :",sum(no))

print("====== using while loop ====")
#while loop
index=0
while index<len(no):
    print(no[index])
    index=index+1

print("======= using for loop ======")
for index in range(len(no)):
    print(no[index])

print("====== for each loop ")
for element in no:
    print(element)

for element in no:
    print(element,":",no.count(element))

#nested list
no=[ [23,33],[344,543,55,65]]

print(no[1][1])
no[1].append(789)
print(no)
no.append(12345)
print(no)

list=[]
for i in range(4):
    list.append(int(input("Enter no:")))

print(list)















