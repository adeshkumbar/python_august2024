#Program to check if the alphabet is Vowel or Consonant

alphabet = input("Enter an alphabet to check if it is a Vowel or Consonant: ")
if len(alphabet) != 1 or not alphabet.isalpha():
        print("Invalid input. Please enter a single alphabetic character.")
else:
    vowels = "aeiouAEIOU"
    if alphabet in vowels:
            print(f"{alphabet} is a vowel.")
    else:
            print(f"{alphabet} is a consonant.")