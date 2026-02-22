# Numbers greater than key value:

l=list(map(int,input("Enter list values:").split()))
k=int(input("Enter key value:"))

for i in l:
    if i>=k:
        print(i,end=" ")

for i in range(len(l)):
    if l[i]>=k:
        print(l[i],end=" ")

# OUTPUT:
# Enter list values:23 43 56 432 3 56 78 986 65 34
# Enter key value:40
# 43 56 432 56 78 986 65


# largest number in a list:

l=list(map(int,input("Enter list values:").split()))
# print(max(l))

res=float('-inf')
for i in range(len(l)):
    if l[i]>res:
        res=l[i]
print(res)

# OUTPUT:
# Enter list values:23 54 234 34 23 75 98
# 234

# second largest number in a list:

l=list(map(int,input("Enter list values:").split()))

max1=float('-inf')
for i in range(len(l)):
    if l[i]>max1:
        max1=l[i]
max2=float('-inf')
for i in range(len(l)):
    if l[i]>max2 and l[i]<max1:
        max2=l[i]
print(max2)

# OUTPUT:
# Enter list values:88 45 1 -98 56 88 86 78 76 67 88 -1000
# 86


# least and second least numbers in a list:

l=list(map(int,input("Enter list values:").split()))

min1=float('inf')
for i in range(len(l)):
    if l[i]<min1:
        min1=l[i]

print("least number is :",min1)

min2=float('inf')
for i in range(len(l)):
    if l[i]<min2 and l[i]>min1:
        min2=l[i]
print("second least number is:",min2)

# OUTPUT:
# Enter list values:23 23 78 98 -98 09 1 
# least number is : -98
# second least number is: 1


# chocolate code:

m=int(input("Enter amount:"))
wrapper=m
choc=m
while wrapper>=3:
    extrac=wrapper//3
    choc+=extrac
    wrapper=extrac+wrapper%3
print("total chocolates:",choc)

# OUTPUT:
# Enter amount:21
# total chocolates: 31
# Enter amount:10
# total chocolates: 14
# Enter amount:1000
# total chocolates: 1499

