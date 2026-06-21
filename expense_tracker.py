def main():
    print("====================================")
    print("   DECODELABS EXPENSE TRACKER       ")
    print("  The Architecture of Financial Truth ")
    print("====================================\n")

    # The Core Skill: The Accumulator Variable
    total_spent = 0.0

    print("Enter your expense amounts below.")
    print("Type 'exit' when you are finished to view the final total.\n")

    while True:
        user_input = input("Enter expense amount ($): ").strip()

        # Check for exit condition
        if user_input.lower() == 'exit':
            break

        try:
            # Convert input to a float for precise math operations
            expense = float(user_input)
            
            if expense < 0:
                print("❌ Expenses cannot be negative. Please enter a valid amount.")
                continue

            # Data Accumulation: total = total + new_expense
            total_spent += expense
            print(f"✅ Added ${expense:.2f}. Current Running Total: ${total_spent:.2f}\n")

        except ValueError:
            print("❌ Invalid input. Please enter a number or type 'exit'.\n")

    # Final Output Display
    print("---")
    print("📊 DATA PROCESSING COMPLETE")
    print(f"💰 Grand Total Spent: ${total_spent:.2f}")
    print("====================================")

if __name__ == "__main__":
    main()