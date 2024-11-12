#list are ordered , changeble , and allow dublicate value list item are indexed
a = ["a","b","c"]
print(a[2])
b = ["d","e"]
a.extend(b)
print(a)

a.pop()
print(a)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)