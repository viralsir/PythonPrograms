'''
  defination : is a sub program which help the main program to get the output.

  def accept argument and return the value.

  syntax :-
            1) defination
             syntax :
                    def  <functionname>(parameter1,parameter2,-----,parameterN):
                        statement
                        return value

            2) calling
                  var=  <functionname>(argument1,argument2,-----,argumentN)

    category of defination
    1)def with argument and with return value
    2)def with argument and without return value
    3)def without argument and with return value
    4)def without argument and without return value


'''

#1)def with argument and with return value
# def total(no1,no2):
#     return no1+no2

#def calling
# sum=total(12,33)
# print("Total :",sum)
# print("avg :",sum/2)


#2) def with argument and without return value
# def total(no1,no2):
#     print("total :",no1+no2)
#
#
# #def calling
# total(33,44)
# total(3,4)

#3)def without argument and with return value

# no1=23
# no2=33
#
# def total():
#     return no1+no2
#
# print("total :",total())


#4) def without argument and witout return value

no1=23
no2=34

def total():
    print("Total :",no1+no2)


total();








