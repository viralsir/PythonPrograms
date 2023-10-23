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

for i in range(3):
    product=[]
    for title in product_title:
        if title=="Name":
            product.append(input("Enter "+title))
        else :
            product.append(int(input("Enter "+title)))

    product.append(product[-2]*product[-1])
    product_list.append(product)

print("\n output :\n")

for product in product_list:
    for  index in range(len(product_title)):
        print(product_title[index],product[index])
    print("Price :",product[-1])
    print("================================")













