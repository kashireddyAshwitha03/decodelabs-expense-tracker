PYTHON EXPENSE TRACKER

Project Overview
This is a simple Expense Tracker application developed using Python as part of the DecodeLabs Industrial Training Kit - Project 2. It tracks ongoing expenses and accumulates them into a running total.

Features
Add new expense amounts

Continuous tracking loop

Automated running total calculation

Error handling for invalid inputs or negative numbers

Clean exit sequence

Technologies Used
Python

Floating-Point Math

While Loops

Conditional Statements (if-else)

Exception Handling (try-except)

How to Run
Download the project files.

Open a terminal in the project folder.

Run:

Bash
python expense_tracker.py
Sample Output
Plaintext
======================================
     DECODELABS EXPENSE TRACKER       
======================================

Enter your expense amounts below.
Type 'exit' when you are finished.

Enter expense amount ($): 45.50
✅ Added $45.50. Current Running Total: $45.50

Enter expense amount ($): hello
❌ Invalid input. Please enter a number or type 'exit'.

Enter expense amount ($): exit

--------------------------------------
📁 DATA PROCESSING COMPLETE
📦 Grand Total Spent: $45.50
======================================
Learning Outcomes
Understanding Data Accumulation concepts (total=total+new_value)

Working with continuous execution loops

Using try-except to prevent program crashes

Validating and filtering user input strings

Managing backend states during runtime

Author
Ashwitha
