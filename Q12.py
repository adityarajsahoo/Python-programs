# Python Program to Print Natural Numbers in Reverse Order

num = int(input("Enter a number: "))
i = num

print("The list of natural numbers from {0} to 1 is: ".format(num))

while(i >= 1):
    print(i, end=" ")
    i = i - 1

# Using max and min

# min = int(input("Enter the minimum number: "))
# max = int(input("Enter the maximum number: "))

# print("The list of natural numbers from {0} to {1}".format(min,max))

# while(max >= min):
#     print(max, end=" ")
#     max = max - 1