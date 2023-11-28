from mylib import checkmarks,isPassFail

#from mylib import *

#import mylib

rollno=int(input("Enter Roll No:"))
rollno=checkmarks(rollno,"Rollno :")
maths=int(input("Enter Maths Mark:"))
maths=checkmarks(maths,"Maths Marks:")
science=int(input("Enter Science Mark:"))
science=checkmarks(science,"Science Marks:")
english=int(input("Enter English Mark:"))
science=checkmarks(science,"English Marks:")

#mylib.checkmarks()

isPassFail(maths,science,english)


