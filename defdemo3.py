'''
  default argument def
'''

def total(no1=0,no2=0,no3=0):
    return no1+no2+no3

print("total :",total(12,22,33))
print("total :",total(12,22))
print("total :",total(12))
print("total :",total())

'''
     you can passing parameter with name 
'''

def sub(no1,no2):
    return no1-no2

print("sub:",sub(345,33))
print("sub:",sub(no2=33,no1=345))


