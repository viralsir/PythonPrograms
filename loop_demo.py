'''

circular control structure :-

       while loop :
          syntax:-
                    initialization of variable
                    while condition :
                         statement
                         increment / decrement of variable


'''
# i=int(input("Enter No:"))
# end=int(input("Enter No:"))
# while i<=end:
#     print(i)
#     i=i+5
# i=1
# sum=0
# while i<=5:
#     no=int(input("Enter No:"))
#     sum=sum+no
#     i=i+1
# print("Sum :",sum)


# no=int(input("Enter No:"))
# start=1
# while start<=250:
#     print(no," * ",start," = ",no*start)
#     start=start+1

# no=int(input("Enter No:"))
# print("divisor:")
# start=1
# while start<=no:
#     if no%start ==0:
#         print(start)
#     start=start+1


no=int(input("Enter No:"))
isPrime=True;
start=2
while start<no:
    if no%start ==0:
        isPrime=False
        break;
    start=start+1
if isPrime==True:
    print(no,"is a prime no")
else :
    print(no,"is not a prime no")



print("outside while loop")













