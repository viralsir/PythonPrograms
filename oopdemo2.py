'''
     class :   is a bunch of related data which are binds together in a single unit.

     object : is a unique medium to access or get the data which are bind to gether in a
     ref class.

     no=1
     no=[13,33,44]
     no={first:13,second:33}

    class student
         rollno
         name
         maths
         sci


         s1=student()
         s2=student()

'''


class student:

    #constructor
    def __init__(self,rollno=0,name="",maths=0,sci=0):
        self.rollno=rollno
        self.name=name
        self.maths=maths
        self.sci=sci


    def entry(self):
        self.rollno = int(input("Enter Roll No:"))
        self.name = input("Enter Student Name:")
        self.maths = int(input("Enter Student Maths :"))
        self.sci = int(input("Enter Student Science :"))

    def view(self):
        print("Roll No:", self.rollno)
        print("Name :", self.name)
        print("Maths :", self.maths)
        print("Sci :", self.sci)


s3=student(4,"vijay",34,44)
# s1=student()
# s1.rollno=23
# print(s1.rollno)

student_list=[]
# s1=student()
# s2=student()


for i in range(3):
    s1=student()
    s1.entry();
    student_list.append(s1)


for s1 in student_list:
    s1.view()








