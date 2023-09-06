'''
    control structure
     conditional control structure

     if
       1)if else
       2)elif
       3)nested if

       syntax :
                    if condition :
                        statement
                        true part
                    else :
                        statement
                        false part

     Relational operator
     operator                   symbol
     grater than                >
     less than                  <
     equal to                   ==
     not equal to               !=
     grater than or
     equal to                   >=
     less than or
     equal to                   <=

     logical operator
     operator           symbol
     and                and
     or                 or
     not                not



'''

no1=int(input("Enter No1:"))
no2=int(input("Enter No2:"))
no3=int(input("Enter No3:"))

if no1>0 and no2>0 and no3>0 :
    if no1>no2 and no1>no3:
        print(no1," is a maximum no")
    elif no2>no1 and no2>no3:
        print(no2," is a maximum no")
    else :
        print(no3,"is a maximum no")
else :
    print("invalid input")



















