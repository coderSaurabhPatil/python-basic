print ("saurabh")
print('saurabh')

#you can assign ultiple line string by three quotes

a = """saurabh
pati"""

print(a)

print(a[2])

#looping throw a string

for x in a:
    print(x)

    #for geting lentgth of string 

print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.

print("saurabh" in a)

#To check if a certain phrase or character is present in a string, we can use the keyword in.

b = "saurabh"

print(b[2:5])
print(b[:5])


#Python - Modify Strings

#Upper Case

print(b.upper())

#Lower Case

print(b.lower())

#Remove Whitespace

#remove from beganing and end 

c = " saurabh "
print(c)
print(c.strip())

#Replace String

print(c.replace("s","S"))

d = "saurabh # patil"
print(d.split("#"))


#Python - Format - Strings

age = 27
txt = f"My name is saurabh age is {age}"
print(txt)