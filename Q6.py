# Python Program to Calculate Electricity Bill

'''
1 to 100 units – Rs. 10/unit
100 to 200 units – Rs. 15/unit
200 to 300 units – Rs. 20/unit
above 300 units – Rs. 25/unit
'''

units = int(input("Enter the number of units consumed: "))

if(units <= 100):
    amt = units * 10
    surcharge = 25
elif(units <= 200):
    amt = 100 * 10 + (units - 100) * 15
    surcharge = 35
elif(units <= 300):
    amt = 100 * 10 + 100 * 15 + (units - 200) * 20
    surcharge = 45
else:
    amt = 100 * 10 + 100 * 15 + 100 * 20 + (units - 300) * 25
    surcharge = 75

total = amt + surcharge
print("\nElectricity Bill = %.2f" %total)

