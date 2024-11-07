def basic_arithmetic_operations():
    print("Basic Arithmetic Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Choose an operation (1-4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        result = num1 + num2
        print(f"Result: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"Result: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"Result: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice!")

def length_converter():
    print("Length Converter")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    
    choice = input("Choose a conversion (1-2): ")
    
    if choice == '1':
        meters = float(input("Enter length in meters: "))
        kilometers = meters / 1000
        print(f"{meters} meters is equal to {kilometers} kilometers.")
    elif choice == '2':
        kilometers = float(input("Enter length in kilometers: "))
        meters = kilometers * 1000
        print(f"{kilometers} kilometers is equal to {meters} meters.")
    else:
        print("Invalid choice!")

def currency_converter():
    print("Currency Converter")
    print("1. Nepali Rupee to Indian Rupee")
    print("2. Indian Rupee to Nepali Rupee")
    print("3. Nepali Rupee to Dollar")
    print("4. Dollar to Nepali Rupee")
    
    choice = input("Choose a conversion (1-4): ")
    
    if choice == '1':
        npr = float(input("Enter amount in Nepali Rupees: "))
        inr = npr / 1.6  # Example conversion rate
        print(f"{npr} NPR is equal to {inr} INR.")
    elif choice == '2':
        inr = float(input("Enter amount in Indian Rupees: "))
        npr = inr * 1.6  # Example conversion rate
        print(f"{inr} INR is equal to {npr} NPR.")
    elif choice == '3':
        npr = float(input("Enter amount in Nepali Rupees: "))
        usd = npr / 130  # Example conversion rate
        print(f"{npr} NPR is equal to {usd} USD.")
    elif choice == '4':
        usd = float(input("Enter amount in Dollars: "))
        npr = usd * 130  # Example conversion rate
        print(f"{usd} USD is equal to {npr} NPR.")
    else:
        print("Invalid choice!")

def number_converter():
    print("Number Converter")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    
    choice = input("Choose a conversion (1-2): ")
    
    if choice == '1':
        binary_number = input("Enter a binary number: ")
        decimal_number = int(binary_number, 2)
        print(f"Binary {binary_number} is equal to Decimal {decimal_number}.")
    elif choice == '2':
        decimal_number = int(input("Enter a decimal number: "))
        binary_number = bin(decimal_number)[2:]
        print(f"Decimal {decimal_number} is equal to Binary {binary_number}.")
    else:
        print("Invalid choice!")

def weight_converter():
    print("Weight Converter")
    print("1. Pound to Kilograms")
    print("2. Kilograms to Pound")
    
    choice = input("Choose a conversion (1-2): ")
    
    if choice == '1':
        pounds = float(input("Enter weight in pounds: "))
        kilograms = pounds * 0.453592
        print(f"{pounds} pounds is equal to {kilograms} kilograms.")
    elif choice == '2':
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms / 0.453592
        print(f"{kilograms} kilograms is equal to {pounds} pounds.")
    else:
        print("Invalid choice!")

def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Basic Arithmetic Operations")
        print("2. Length Converter")
        print("3. Currency Converter")
        print("4. Number Converter")
        print("5. Weight Converter")
        print("6. Exit")

        option = input("\nSelect an option (1-6): ")

        if option == '1':
            basic_arithmetic_operations()
        elif option == '2':
            length_converter()
        elif option == '3':
            currency_converter()
        elif option == '4':
            number_converter()
        elif option == '5':
            weight_converter()
        elif option == '6':
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()