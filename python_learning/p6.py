#Program to check if the alphabet is uppercase

alphabet = input("Enter an alphabet: ")
if len(alphabet) != 1 or not alphabet.isalpha():
        print("Invalid input. Please enter a single alphabetic character.")
else:
        if alphabet .isupper():
            print(f"The alphabet '{alphabet}' is an uppercase letter.")