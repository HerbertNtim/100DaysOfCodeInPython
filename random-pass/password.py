import random

print("Welcome To Random Password Generator")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = [
  "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
  "[", "]", "{", "}", ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?", "\\", "|", "`", "~"
]

user_passwordType = input("Type 'easy' or 'hard':\n").lower()
user_letters = input("Enter the number of letter you want in Password:\n")
user_numbers = input("Enter the number of numbers you want in Password:\n")
user_symbols = input("Enter the number of symbols you want in Password:\n")

# Easy way

if user_passwordType == "easy":
  password = ''
  for char in range(1, int(user_letters) + 1):
    password += random.choice(letters)

  for number in range(1, int(user_numbers) + 1):
    password += random.choice(numbers)

  for symbol in range(1, int(user_symbols) + 1):
    password += random.choice(symbols)

  print(f"Your Password is: {password}")


# Hard way
if user_passwordType == "hard":
  password_list = []
  for char in range(1, int(user_letters) + 1):
    password_list += random.choice(letters)

  for number in range(1, int(user_numbers) + 1):
    password_list += random.choice(numbers)

  for symbol in range(1, int(user_symbols) + 1):
    password_list += random.choice(symbols)

  random.shuffle(password_list)
  password = ''.join(password_list)
  print(f"Your Password is: {password}")

