name="Hello World @123"
print(name)
print(name[0])
print(name[-1])
print(name[0:3])
print(name[0:7:2])
print(name[::-1])

name2=name+" pyhton"
print(name2)
name3=name2*2
print(name3)

print("upper case :",name.upper())
print("lower case :",name.lower())
print("title case :",name.title())
print("capitalize :",name.capitalize())
print("find :",name.find('o'))
print("find :",name.find('o',5))
print("count :",name.count('l'))
print("split :",name.split(" "))

if name.isupper():
    print("name is in upper case ")
elif name.islower():
    print("name is in lower case")
elif name.istitle():
    print("name is in title case ")

if name.isalpha():
    print("all are character ")
elif name.isnumeric():
    print("all are numeric ")
elif name.isalnum():
    print("it contain character and numeric both")
else :
    print("it contains character,symbol and numeric ")


for character in name:
    if character.isalpha():
         print(character,"- alphabet")
    elif character.isnumeric():
        print(character," - numeric ")
    elif character.isspace():
        print(character," - space")
    else :
        print(character," - symbol")





