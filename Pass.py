import random
import string
print("Welcome to the Password Generator ..!")
length = int(input("Enter The Total Number of Characters in the Password : "))

letters_num = int(input("Enter The letters in the password :"))
number = int(input("Enter The Number in the Password :"))
symbols_num = int(input("Enter The Symbols in the password :"))

if length != (letters_num + number + symbols_num):
    print("Invalid Password Please Try Again ")
else:
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password = (
            random.choices(letters, k=letters_num) +
            random.choices(numbers, k=number) +
            random.choices(symbols, k=symbols_num)
                )
    random.shuffle(password)
    password_chars = "".join(password)

    print("Generated Password : ", password_chars)
