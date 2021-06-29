# Here i will create a two types of list and then sort them in ascending order 

# First is where I create the list here itself and do sorting in it 

l = [32,56,79,23,12,35,57,24,65]

l.sort()

print(l)

# Second one is where u can give input and then it will do sorting

print("Enter the lenght of the list: ")

n = int(input())

l1 = []

print("Enter any number of your choice")
for i in range(n):
    s = int(input())
    l1.append(s)
l1.sort()
print(l1)