#Program to Print Math table of a number

number = input("Enter a number :")
if  number.isdigit() == True:
    input_number = int(number)
    print("TABLE:\n")
    for integer in range(1,11):
        print(input_number,"X",integer,"=",input_number*integer)
else:
        print("Invalid input.Please enter a valid number")