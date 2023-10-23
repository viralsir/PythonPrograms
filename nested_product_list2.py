'''

Student_list =[
                [1,"vimal",23,33,44],
                [2,"viren",32,33,44],
                [3,"vijay",34,44,55]
                ]

student_div_list=[ [ [],[],[] ,[] ] , [ [],[],[],[] ]  ,[[], []]  ]


product_list=[ [] ,[],[],[] ,[], []  ]

'''
product_list=[]
product_title=["Id","Name","Qty","Rate"]

option2=1
while option2!=3:
    print("\t\t\t Product Menu")
    print("\t\t press 1 for Entry ")
    print("\t\t press 2 for View ")
    print("\t\t press 3 for Exit")

    option2 = int(input("Enter Your option :"))

    if option2==1 :

        option='y'
        while option=='Y' or option=='y':
            product=[]
            for title in product_title:
                if title=="Name":
                    product.append(input("Enter "+title))
                else :
                    product.append(int(input("Enter "+title)))

            product.append(product[-2]*product[-1])
            product_list.append(product)
            option=input("do you want to continue (y/n)?:")
    elif option2==2:

        print("\n output :\n")

        for product in product_list:
            for  index in range(len(product_title)):
                print(product_title[index],product[index])
            print("Price :",product[-1])
            print("================================")
    elif option2==3:
        print("you are exit ")
    else :
        print("wrong option selected try again !")













