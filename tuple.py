#tuple are orderd and unchangeble and allow duplicate

a = ("a" , "b")
print(len(a))

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#unpacking 

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

