#open file in write only mode
#f=open("first.txt","w")
#open file in append only mode
# f=open("first.txt","a")
#
# #save or write content into file
# print(" to the world of python",file=f,end=" ")
# #close the file
# f.close()


#open file in read only mode
f=open("first.txt","r")

# for line in f:
#     print(line)
print(f.read())


