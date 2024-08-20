#Program to check if user given year is a Leap year.

Year = input("Enter a number to check if the year is a leap year:")
if  Year.isdigit() == True:
    input_year = int (Year)
    if (input_year % 4 == 0) and ((input_year % 400 == 0) or (input_year % 100 != 0) ):
        print(f"{input_year} is a Leap Year")
else:
        print("Invalid input.Please enter a valid number")