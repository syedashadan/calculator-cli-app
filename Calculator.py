import time
import math

history = []
last_result = None

def loading():
    print("⏳ Calculating", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print()

def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("❌ Please enter a valid number!")

def show_menu():
    print("\n✨ UltraCalc CLI ✨")
    print("1 ➕ Add")
    print("2 ➖ Subtract")
    print("3 ✖ Multiply")
    print("4 ➗ Divide")
    print("5 🔢 Power")
    print("6 📜 History")
    print("7 🚪 Exit")

while True:
    show_menu()
    choice = input("👉 Choose: ")

    if choice in ['1','2','3','4','5']:
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        loading()

        if choice == '1':
            result = a + b
            op = "+"
        elif choice == '2':
            result = a - b
            op = "-"
        elif choice == '3':
            result = a * b
            op = "*"
        elif choice == '4':
            result = "❌ Cannot divide by zero!" if b == 0 else a / b
            op = "/"
        elif choice == '5':
            result = a ** b
            op = "^"

        print(f"🎉 Result: {result}")
        history.append(f"{a} {op} {b} = {result}")
        last_result = result

    elif choice == '6':
        print("\n📜 History:")
        if not history:
            print("No history yet.")
        else:
            for h in history:
                print("•", h)

    elif choice == '7':
        print("👋 Goodbye! Stay awesome!")
        break

    else:
        print("❌ Invalid choice!")

