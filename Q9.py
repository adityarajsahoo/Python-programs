# Python Program to find Largest of Two Numbers

a = float(input("Enter the First number: "))
b = float(input("Enter the Second number: "))

if(a > b):
    print(a, "is the largest number")
elif(b > a):
    print(b, "is the largest number")
else:
    print("Both the numbers are equal")