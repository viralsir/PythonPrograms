def isPositive(no):
    if no>0:
        return True
    else :
        return False

# def maximum(no1,no2):
#     if no1>no2:
#         print(no1," is a maximum")
#     else :
#         print(no2," is a maximum")


def maximum(no1,no2):
    if isPositive(no1) and isPositive(no2):
        if no1>no2:
            print(no1," is a maximum")
        else :
            print(no2," is a maximum")
    else :
        print("nagetive no are not allowed")

def factorial(no1):
    fact=1
    for i in range(1,no1+1):
        fact=fact*i;

    return fact

def no_of_digit(no):
    count=0
    while no>0:
        count=count+1
        no=no//10
    return count



i=int(input("Enter No:"))
j=int(input("Enter No:"))
# if isPositive(i)==True  and isPositive(j)==True:
#     maximum(i,j)
# else :
#     print("nagetive no are not allowed")

maximum(i,j)
print("Factorial of ",i," is ",factorial(i))
print("Factorial of ",j," is ",factorial(j))
print("no of digit :",no_of_digit(i))