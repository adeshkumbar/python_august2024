#Accept a number as input,say X and define a logic to get the output say Y.The input can be only 0 or 1 and the output must be 1 if input is 0 and viceversa
X=int(input("Enter a number(0 or 1 only):"))
if X==0 or X==1:
    Y=1-X
    print(f'Input Number: {X}, Output Number:{Y}')
else:
    print("Invalid Number")