#program to accept 3 distinct number and find smallest among them.
print("Enter three distinct numbers\n")
input_num1=int(input("Enter first number:"))
input_num2=int(input("Enter second number:"))
input_num3=int(input("Enter third number:"))
if input_num1<input_num2 and input_num1<input_num3:
    print(f'{input_num1} is smallest')
elif input_num2<input_num3:
    print(f'{input_num2} is smallest')
else:
    print(f'{input_num3} is smallest')
