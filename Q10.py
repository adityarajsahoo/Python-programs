# Python Program to find Largest of Three Numbers using Elif Statement

a = float(input("Enter the First number: "))
b = float(input("Enter the Second number: "))
c = float(input("Enter the Third number: "))

# print(max(a,b,c), "is the largest number") Soln 1

# Soln 2

if(a>b and a>c):
    print(a, "is the largest number")
elif(b>c and b>a):
    print(b, "is the largest number")
elif(c>a and c>b):
    print(c, "is the largest number")
else:
    print("All the numbers are equal")