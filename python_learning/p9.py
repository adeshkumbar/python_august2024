#Program to Print Math table of a number

number = input("Enter a number to print its MATH Table :")
if  number.isdigit() == True:
    input_number = int(number)
    print("TABLE:\n")
    for integer in range(1,11):
        print('%02d * %02d = %03d'%(input_number,integer,input_number*integer))
else:
        print("Invalid input.Please enter a valid number")
