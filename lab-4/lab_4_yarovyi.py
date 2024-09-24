def print_colored_text(text):
    reset = "\033[0m"
    green = "\033[32m"
    print(f"{green}{text}{reset}")


# 1
print_colored_text("task --> 1")
n = int(input("Введіть число: "))
print(n >= 100)

# 2
print_colored_text("task --> 2")
a = float(input("Введіть 1-ше дійсне число: "))
b = float(input("Введіть 2-ге дійсне число: "))

if a > b:
    print("Найбільше число:", a)
else:
    print("Найбільше число:", b)

# 3
print_colored_text("task --> 3")

input_string = input("Введіть слово: ")

if input_string == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif input_string == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {input_string}!")

# 4
print_colored_text("task --> 4")

income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# 5
print_colored_text("task --> 5")

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period.")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")

# 6
print_colored_text("task --> 6")

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    guess = int(input("Введіть ціле число: "))

    if guess != secret_number:
        print("Ха-ха! Ви застрягли у моїй петлі!")
    else:
        print(f"Молодець, магле! Тепер ти вільний. Загаданне число: {secret_number}")
        break

# 7
print_colored_text("task --> 7")

import time

for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

# 8
print_colored_text("task --> 8")

while True:
    word = input("Введите слово: ")

    if word == "chupacabra":
        print("You've successfully left the loop.")
        break

# 9
print_colored_text("task --> 9")

user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
#    if letter in ['A', 'E', 'I', 'O', 'U']:
#        continue
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
      print(letter)

# 10
print_colored_text("task --> 10")

word_without_vowels = ""

user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)

# 11
print_colored_text("task --> 11")

blocks = int(input("Введіть кількість блоків: "))

pyramid_height = 0
layer = 1
height_one_layer = 1

while blocks >= layer:
    blocks -= layer
    layer += 1
    pyramid_height += height_one_layer

print(f"The height of the pyramid: {pyramid_height}")

# 12
print_colored_text("task --> 12")

c0 = int(input("Введіть натуральне число: "))

steps = 0
while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
print(c0)

print(f"Кількість кроків для досягнення 1: {steps}")

