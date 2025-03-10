import calculator

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Percentage")
    print("7. Factorial")
    print("8. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")
    
    if choice == '8':
        print("Exiting calculator... Goodbye! 😊")
        break
    try:
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        percent = float(request.form.get('percent', 0))
    except ValueError:
        result = "Invalid input"

    if choice == '7':
        num = int(input("Enter a number for factorial: "))
        print(f"{num}! = {calculator.factorial(num)}")
        break
    else:
        num1 = float(input("Enter first number: "))

        if choice == '6':
            percent = float(input("Enter percentage value: "))
            print(f"{percent}% of {num1} = {calculator.percentage(num1, percent)}")
        else:
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {calculator.add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} × {num2} = {calculator.multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} ÷ {num2} = {calculator.divide(num1, num2)}")

            elif choice == '5':
                print(f"{num1} ^ {num2} = {calculator.square(num1, num2)}")

            else:
                print("Invalid input! Please choose a valid option.")
