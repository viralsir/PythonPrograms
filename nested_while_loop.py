'''
nested while

i=5
while i>=1:
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    print("")
    i=i-1
'''
no=int(input("Enter No:"))  # 5 -> 9 6 ->11  7 -> 13

i=1
k=1
while i<=2*no-1 :
    j=no+1
    while j>=1:
        if j>k:
            print(" ",end="")
        else :
            print(j,end="")
        j=j-1
    print("")
    if i<no:
        k=k+1
    else:
        k=k-1
    i=i+1


'''
 - - - - - 1
 - - - - 2 1
 - - - 3 2 1
 -- 4 3 2 1
- 5 4 3 2 1
'''
