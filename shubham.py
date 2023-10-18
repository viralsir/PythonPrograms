x = int(input("What is the first number? "))
y = int(input("What is the second number? "))
answer = 0

while y != 0:
   if (y%2 != 0):
      answer=answer+x

   x=x*2
   y=y//2


print("the product is",(answer))