print("===== Expense Tracker =====")

total = 0

while True:
    expense = float(input("Enter expense amount: "))
    total = total + expense

    choice = input("Do you want to add another expense? (Y/N): ").lower()

    if choice == "n":
        break


print("\n===== Expense Summary =====")
print("Total Spent: Rs.", total)
print("Thank you for using Expense Tracker!")
