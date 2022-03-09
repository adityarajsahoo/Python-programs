# Python Program to find Compound Interest

import math

Principal_Amt = float(input("Enter the Principal Amount: "))
Rate_of_Interest = float(input("Enter the Rate of Interest: "))
Time_Period = float(input("Enter the Time Period in Years: "))

CI_Future = Principal_Amt * (math.pow((1 + Rate_of_Interest/100), Time_Period))
Compound_Interest = CI_Future - Principal_Amt

print("Future Compound Interest for Principal Amount {0} = {1}".format(Principal_Amt,CI_Future))
print("Compound Interest for Principal Amount {0} = {1}".format(Principal_Amt,Compound_Interest))