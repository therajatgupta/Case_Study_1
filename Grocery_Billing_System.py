# -----------------------------------------------------------
# Grocery Billing System
# Name: Rajat Gupta
# Roll No: 202501100700114
# Branch: ECE-B
# -----------------------------------------------------------

#demo change

# Step 1: Ask user for number of different items
items = int(input("Enter number of items in the bill: "))

# Step 2: Store per-unit price of each item in a dictionary
prices = {}

for i in range(items):
    prices[i + 1] = int(input(f"Enter price of item-{i + 1}: "))

# Step 3: Ask quantity of each item and calculate gross amount
gross_amount = 0.0

for i in range(items):
    quantity = int(input(f"Enter quantity of item-{i + 1}: "))
    gross_amount += prices[i + 1] * quantity

# Display gross amount
print("\n-----------------------------------")
print(f"Gross Amount (before discount): ₹{gross_amount}")
print("-----------------------------------")

# Step 4: Apply discount if applicable
if gross_amount > 100:
    discount = gross_amount * 0.10   # 10% discount
else:
    discount = 0.0

# Display discount
print(f"Discount Applied: ₹{discount}")

# Step 5: Calculate final payable amount
final_amount = gross_amount - discount

# Display final bill amount
print(f"Final Amount to Pay: ₹{final_amount}")
print("-----------------------------------")
print("Thank you for shopping with us!")