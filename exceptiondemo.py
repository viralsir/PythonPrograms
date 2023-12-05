'''
exception : is the message which is being display when runtime error is occured.
excption handling

try
except

'''
iserror=True
while iserror:
    try:
        no1=int(input("Enter No1:"))
        no2=int(input("Enter No2:"))

        ans=no1/no2;

        print("Answer :",ans)
        iserror=False;
    except ZeroDivisionError:
        print("zero is invalid as a no2")
    except ValueError:
        print("character are not allowed.")
    finally:
        print("finally is executed")

print("end program")