name = "harshit"
for i in range(len(name)):
    print(name[i])

# another way
name="harshit"
for i in name:
    print(i)

# another way
for i in "mohit":
    print(i)

# 1256 --->1+2+5+6

num=input("enter a number: ")
total = 0
for i in num:
    total+=int(i)
print(total)