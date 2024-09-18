
ratePerUnit = float(290.5)
dateOfBill = str("18th September, 2024")

print("\nEnter the following details below.\n")
customerName = input("Customer Name: ")
accountNumber = input("Account Number: ")
unitsConsumed = float(input("Units Consumed: "))  # Convert to float directly here

# Calculate tax and billed amount based on units consumed
if unitsConsumed >= 50000:
    taxRate = 0.2
    taxAmount = taxRate * unitsConsumed
    billedAmount = unitsConsumed * ratePerUnit
elif 27000 <= unitsConsumed < 50000:
    taxRate = 0.125
    taxAmount = taxRate * unitsConsumed
    billedAmount = unitsConsumed * ratePerUnit
elif 5000 <= unitsConsumed < 27000:
    taxRate = 0.065
    taxAmount = taxRate * unitsConsumed
    billedAmount = unitsConsumed * ratePerUnit
else:
    taxRate = 0
    taxAmount = 0
    billedAmount = unitsConsumed * ratePerUnit  # Corrected calculation

# Calculate total bill
totalBill = billedAmount + taxAmount  # Corrected total bill calculation

# Print the bill details
print("\n********** UMEME CUSTOMER MONTHLY BILL **********")
print("Date of Bill   : ", dateOfBill)
print("Customer Name  : ", customerName.upper())
print("Account Number : ", accountNumber)
print("Units Consumed : ", unitsConsumed, " Units.")
print("Rate per Unit  : ", ratePerUnit, " UGX.")
print("Tax Rate       : ", taxRate, "%.")
print("Tax Amount     : ", taxAmount, " UGX.")
print("Billed Amount  : ", billedAmount, " UGX.")
print("Total Bill     : ", totalBill, " UGX.")

print("\n********** Thank You for being a responsible customer **********")
