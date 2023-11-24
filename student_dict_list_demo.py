'''
    Student_list=[{rollno,name,maths,sci,eng},{},{}]

    level - 0 : add search option in  menu display record search by rollno
    level - 1 : add pass/fail option in menu
    level - 2 : change the program structure such that way that student info will be store division wise.


'''
studentlist=[]
titlelist=["Roll No:","Name:","Maths:","Science:","English:","Physics:"]
option=1
while option!=3:
    print("\t\t\t Student Info")
    print("\t\t press 1 for Entry")
    print("\t\t press 2 for View")
    print("\t\t press 3 for Exit")

    option=int(input("\t Enter Your option :"))

    if option==1:
         option2="y"
         while option2.lower()=="y":
            student={}
            for t in titlelist:
                if t=="Name:":
                    student[t]=input("Enter Name :")
                else :
                    if t=="Roll No:":
                        student[t]=int(input("Enter "+t))
                    else :
                        student[t] = int(input("Enter " + t))
                        while not 0<=student[t]<=100:
                            print("invalid marks")
                            student[t] = int(input("Enter " + t))

            studentlist.append(student)
            option2=input("Do you want to Continue?(y/n):")
    elif option==2:
         for student in studentlist:
            is_pass=True
            total=0
            for key,value in student.items():
                print(key,value)
                if key !="Roll No:" and key!="Name:":
                   total=total+value
                   if value<35 :
                       is_pass=False

            if is_pass==True:
                print("you are pass")
                print("Total :",total)
                print("avg :",total/4)

            else :
                print("you are fail")
            print("========================")
    elif option==3:
        print("\n you are exited")
    else :
        print("Wrong option selected try again!!!")
