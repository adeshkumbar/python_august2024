#Program to check if a number is Perfect Square

number = input("Enter a number to check if the number is a perfect square:")
if  number.isdigit() == True:
    input_number = int(number)
    if input_number % (input_number**0.5) == 0:
        print(f"{input_number} is a perfect square")
else:
        print("Invalid input.Please enter a valid number")