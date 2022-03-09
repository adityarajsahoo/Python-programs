# 19BEI0086
# Python Program to find the 2nd biggest element in an array.

arr = []
n = int(input("Enter number of elements: "))
for i in range(1,n+1):
  b = int(input())
  arr.append(b)
print(arr)
arr.sort()
x = len(arr)

if(x<2):
    print("Invalid Input")

first = second = -101
for i in range (x):
    if[arr[i]>first]:

        second = first
        first = arr[i]

    elif(arr[i]>second and arr[i]!=first):
        second = arr[i]

if(second == -101):
    print("There is no second largest")
else:
    print("The second largest element is", second)
