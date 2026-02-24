🛒 Grocery Billing System

Name: Rajat Gupta Roll No: 202501100700114 Branch: ECE-B

------------------------------------------------------------------------

Problem Statement: The Grocery Billing System is a simple Python program
designed to calculate the total bill amount for a customer purchasing
multiple grocery items.

The program: - Takes the number of items as input. - Accepts per-unit
price for each item. - Accepts quantity for each item. - Calculates the
gross amount. - Applies a 10% discount if the gross amount exceeds
₹100. - Displays the final payable amount.

------------------------------------------------------------------------

How the Program Works:

Step 1: Input Number of Items The user enters how many different items
are included in the bill.

Step 2: Input Item Prices The program asks for the price of each item
and stores them.

Step 3: Input Item Quantities The program asks for quantity of each item
and calculates total.

Step 4: Calculate Gross Amount Gross amount = Sum of (price × quantity
for each item)

Step 5: Apply Discount If total amount > ₹100 → 10% discount is applied
Otherwise → No discount

Step 6: Display Final Amount Final amount = Gross amount − Discount

------------------------------------------------------------------------

How to Run the Program:

1.  Save the code in a file named: grocery_billing_system.py

2.  Open terminal or command prompt.

3.  Navigate to the file location.

4.  Run the program using: python grocery_billing_system.py

5.  Follow the on-screen instructions.

------------------------------------------------------------------------

Sample Input & Output:

Sample Run 1 (Discount Applied):

Enter no of items: 2 Enter item-1 price: 50 Enter item-2 price: 40 Enter
item-1 quantity :2 Enter item-2 quantity :1

Output: Gross amount (before discount): 140.0 Discount (if applicable):
14.0 Final amount (after discount if applicable) 126.0

------------------------------------------------------------------------

Sample Run 2 (No Discount):

Enter no of items: 1 Enter item-1 price: 80 Enter item-1 quantity :1

Output: Gross amount (before discount): 80.0 Discount (if applicable):
0.0 Final amount (after discount if applicable) 80.0

------------------------------------------------------------------------

Concepts Used: - Dictionary - for loops - if-else - Arithmetic
operations - input() function - Type casting

------------------------------------------------------------------------

Conclusion: This Grocery Billing System demonstrates basic programming
logic and user interaction in Python. It is ideal for beginners to
understand how billing systems work and implement discount logic.
