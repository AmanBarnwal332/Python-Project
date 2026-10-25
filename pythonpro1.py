correct_pin = "1234"
balance = 10000
attempts = 3
transactions = []

while attempts > 0:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == correct_pin:
        print("PIN accepted!")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print("Wrong PIN. Attempts left:", attempts)
        else:
            print("Card blocked.")
else:
    exit()
while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    option = input("Enter your option: ")
    if option == "1":
        print("Current balance:", balance)
    elif option == "2":
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposit {amount}")
            print("New balance:", balance)
        else:
            print("Amount must be above 0")

    elif option == "3":
        amount = int(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be above 0")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            transactions.append(f"Withdraw {amount}")
            print("New balance:", balance)

    elif option == "4":
        print("Thank you!")
        print("Transaction history:")
        for transaction in transactions:
            print(transaction)
        break
    else:
        print("Invalid option. Please try again.")


