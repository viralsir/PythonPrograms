rollno=[]
name=[]
maths=[]
sci=[]

#student=[1,"vimal",23,33,2,"viren",33,44]


for i in range(3):
    rollno.append(int(input("Enter Roll No:")))
    name.append(input("Enter Name:"))
    maths.append(int(input("Enter Maths Marks:")))
    sci.append(int(input("Enter Science Marks:")))


print("\n output :\n")

for r,n,m,s  in zip(rollno,name,maths,sci):
    print("Roll No:",r)
    print("Name :",n)
    print("Maths :",m)
    print("Science :",s)


