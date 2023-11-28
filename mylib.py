PASSING_MARKS=35
def checkmarks(mark,subject):
    while not 0<=mark<=100:
        print("invalid "+subject)
        mark=int(input("Enter "+subject))

    return mark


def isPassFail(maths,sci,eng):
    if maths>=PASSING_MARKS and sci>=PASSING_MARKS and eng>=PASSING_MARKS :
        print("you are pass")
        total=maths+sci+eng
        avg=total/3
        print("Total :",total)
        print("Avg :",avg)
        Grade(avg)
    else :
        print("you are fail")


def Grade(avg):
    if avg>=90:
        print("Grade :A")
    elif avg>=75:
        print("Grade :B")
    elif avg>=60 :
        print("Grade :C")
    else :
        print("Grade :D")
