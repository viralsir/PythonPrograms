'''
dictionary : { key:value , key:value}

'''
# dict1={1:"first","second":2,3:34.444}
#
# print(dict1)
# print(dict1[1])
# print(dict1['second'])
# #print(dict1['6'])
#
# dict1[1]="one"
# print(dict1)
# dict1[4]='fourth'
# print(dict1)
# dict1[5]=input("Enter value :")
# print(dict1)
#
# for key in range(6,9):
#     dict1[key]=int(input("Enter no:"))
#
# print(dict1)

# person={}
# person["name"]=input("Enter Name:")
# person["city"]=input("Enter city:")


# person={"name":"vimal","city":"Ahmedabad"
#         ,"phno":[2323233,4545444]
#         }
#
# person={"name":"vimal","city":"Ahmedabad"
#         ,"phno":{"home":2323233,"office":4545444}
#         }
#
# print(person)
# print(person["name"])
# print(person["city"])
# print(person["phno"])
# #print(person["phno"][0])
# print(person["phno"]["home"])
#
# print("all keys :")
# for key in person:
#     print(key)
# print("all values :")
# for value in person.values():
#     print(value)
# print("all items :")
# for key,value in person.items():
#     print(key,value)


# person_list=[{"name":"vimal","city":"Ahmedabad","phno":343434},
#              {"name":"viren","city":"baroda","phno":343434},
#              {"name":"vijay","city":"gandhinagar","phno":343433}
#             ]
#
# print(person_list[1]["name"])
#
# for element in person_list:
#     #print(element)
#     for key ,value in element.items():
#         print(key," - ", value)
#     print("================")
#

person_list=[]

#for i in range(3):
option="y"
while option.lower()=="y":
    person={}
    person["name"]=input("Enter Name :")
    person["city"]=input("Enter City:")
    person_list.append(person)
    option=input("do you want to continue(y / N):")



for element in person_list:
    #print(element)
    for key ,value in element.items():
        print(key," - ", value)
    print("================")
#


