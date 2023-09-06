PASSING_MARK=34
rollno=int(input("Enter Roll No:"))
name=input("Enter Name:")
maths=int(input("Enter Maths Marks:"))
sci=int(input("Enter Science Marks:"))
eng=int(input("Enter English Marks:"))


print("output :\n")
print("Roll No:",rollno)
print("Name :",name)
print("Maths :",maths)
print("Science :",sci)
print("English:",eng)

if maths>=PASSING_MARK and sci>=PASSING_MARK and eng>=PASSING_MARK:
    print("you are pass")
    total=maths+sci+eng
    avg=total/3
    print("total :",total)
    print("avg :",avg)
    if avg>=90:
        print("Grade :A")
    elif avg>=70:
        print("Grade:B")
    elif avg>=55:
        print("Grade:C")
    else :
        print("Grade:D")
else :
    print("you are fail")