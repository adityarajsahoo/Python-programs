# Program to Perform Arithmetic Operations

N1 = float(input("enter the first number: "))
N2 = float(input("enter the second number: "))

# Add Two Numbers
add = N1 + N2

# Subtracting N2 from N1
sub = N1 - N2

# Multiply N1 with N2
multi = N1 * N2

# Divide N1 by N2
div = N1 / N2

# Modulus of N1 and N2
mod = N1 % N2

# Exponent of N1 and N2
expo = N1 ** N2

print("The Sum of {0} and {1} = {2}".format(N1, N2, add))
print("The Subtraction of {0} from {1} = {2}".format(N1, N2, sub))
print("The Multiplication of {0} and {1} = {2}".format(N1, N2, multi))
print("The Division of {0} and {1} = {2}".format(N1, N2, div))
print("The Modulus of {0} and {1} = {2}".format(N1, N2, mod))
print("The Exponent Value of {0} and {1} = {2}".format(N1, N2, expo))