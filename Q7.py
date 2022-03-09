# Python Program to Calculate Simple Interest

Principal_Amt = float(input("Enter the Principal Amount: "))
Rate_of_Interest = float(input("Enter the Rate of Interest: "))
Time_Period = float(input("Enter the Time Period in Years: "))

Simple_Interset = (Principal_Amt*Rate_of_Interest*Time_Period)/100

print("\nSimple Interest for Principal Amount {0} = {1}".format(Principal_Amt,Simple_Interset))
