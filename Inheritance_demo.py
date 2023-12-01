'''

DataBase connectivity :

django


Inheritance : is the proccess by which object
of one class can access or get the properties of
object of another class.

exp

Class A:    parent class or base class or super class
  noA=34

Class B (A): child class or derived class or sub class
  noB=3444

a1=A()
a1.noA
a1.noB


b1=B()
b1.noB
b1.noA


    category of inheritance

1)Single Inheritance :  one object can access or get the properties of only one
object at a time .

            A
            |
            B

2)Multilevel Inheritance : contious chain of single inheritance

     A
     |
     B
     |
     C

3)Hyrarchical Inheritance : more than one object access or get the properties
of same object .
                         A
                    |        |
                    B       C

4)Multiple Inheritance :one object can access or get the properties of more
than one  object at a time

                     A             B
                            |
                            C

5)hybrid Inheritance :- combination of more than one inheritance  is called
hybrid inheritance

                            PersonalInfo
                              |
                   Employee           Customer
                       |               |
                              Dmart

'''

class Personal_Info:
    id=0
    name=""
    address=""

    def setPersonal_Info(self):
        self.id=int(input("Enter Id:"))
        self.name=input("Enter Name:")

        self.address=input("Enter Address:")

    def getPersonal_Info(self):
        print("Id :",self.id)
        print("Name :",self.name)
        print("Address:",self.address)


class Employee(Personal_Info):
    salary=0

    def setSalary(self):
        self.salary=int(input("Enter Salary:"))

    def getSalary(self):
        print("Salary :",self.salary)

class Customer(Personal_Info):
    billamount=0

    def setBillAmount(self):
        self.billamount=int(input("Enter Bill Amount :"))

    def getBillAmount(self):
        print("Bill Amount :",self.billamount);


class Dmart(Employee,Customer):
    location=""

    def setLocation(self):
        self.location=input("Enter Location :")

    def getLocation(self):
        print("Location :",self.location)






# e1=Employee()
# e1.setPersonal_Info()
# e1.setSalary()
#
# e1.getPersonal_Info()
# e1.getSalary()

# dmart=Dmart()
# dmart.setPersonal_Info()
# dmart.setSalary()
# dmart.setLocation()
#
#
# dmart.getPersonal_Info()
# dmart.getSalary()
# dmart.getLocation()


print("=== Employee ===")
e1=Employee()
e1.setPersonal_Info()
e1.setSalary()

print("===== Customer ====")
c1=Customer()
c1.setPersonal_Info()
c1.setBillAmount()







