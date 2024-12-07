def print_colored_text(text):
    reset = "\033[0m"
    green = "\033[32m"
    print(f"{green}{text}{reset}")

# 1
print_colored_text("example --> 1")

# Написати метод аналогічний split()

# I варінат (некрасивий, але, можливо, оптимальніший, ніж ІІ)
# def mysplit(string):
#     string = string.lstrip() # метод strip() не змінює об'єкт, а створює копію!

#     list_split = []

#     if string.isspace() or string == "": # якщо рядок пустий, або з одних пробілів
#         return list_split

#     if string.find(' ') == -1: # якщо з одного слова
#         list_split.append(string)
#         return list_split

#     fnd_1 = 0
#     fnd_2 = string.find(' ')

#     while fnd_2 != -1:
#         list_split.append(string[fnd_1:fnd_2])
#         fnd_1 = fnd_2
#         fnd_2 = string.find(' ', fnd_2 + 1)

#     return list_split

# ІІ варіант (красивий, але не факт, що оптимальний)

def mysplit(string):
    list_split = []
    word = ""
    for char in string:
        if char == " ":
            if word:
                list_split.append(word)
            word = ""
        else:
            word += char
    if word:
        list_split.append(word)
    return list_split


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

# 2
print_colored_text("example --> 2")

# number_input = input('Введіть ціле число: ')
# number_list = [str(i) for i in range(0, 10)]
number_dict = {'1' : ('  #', '  #', '  #', '  #', '  #'),
               '2' : ('###', '  #', '###', '#  ', '###'),
               '3' : ('###', '  #', '###', '  #', '###'),
               '4' : ('# #', '# #', '###', '  #', '  #'),
               '5' : ('###', '#  ', '###', '  #', '###'),
               '6' : ('###', '#  ', '###', '# #', '###'),
               '7' : ('###', '  #', '  #', '  #', '  #'),
               '8' : ('###', '# #', '###', '# #', '###'),
               '9' : ('###', '# #', '###', '  #', '###'),
               '0' : ('###', '# #', '# #', '# #', '###')
               }
def display_number(num):
    if num < 0:
        print("Число має бути невід'ємним.")
        return

    num_str = str(num)

    for level in range(5):
        for simbol in num_str:
            print(number_dict[simbol][level], end=' ')
        print()

display_number(12345)

# 3
print_colored_text("example --> 3")

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# 4
print_colored_text("example --> 4")

# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

# 5
print_colored_text("task --> 1")


def caesar_cipher_encrypt(text, shift):
    """Шифрує текст шифром Цезаря зі збереженням регістру та обробкою неалфавітних символів."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Визначаємо базовий код символу ('A' для великих і 'a' для малих)
            base = ord('A') if char.isupper() else ord('a')
            # Застосовуємо зсув
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += new_char
        else:
            # Неалфавітні символи залишаємо без змін
            encrypted_text += char
    return encrypted_text


def main():
    """Основна функція для отримання вводу та виводу результату."""
    text = input("Введіть текст для шифрування (для тесту \"Hello, World!\"): ")
    while True:
        try:
            shift = int(input("Введіть значення зсуву (1-25) (для тесту 3): "))
            if 1 <= shift <= 25:
                break
            else:
                print("Зсув має бути у межах 1-25. Спробуйте ще раз.")
        except ValueError:
            print("Некоректне значення. Введіть ціле число.")

    encrypted_text = caesar_cipher_encrypt(text, shift)
    print(f"Зашифрований текст (для тесту буде \"Khoor, Zruog!\"): {encrypted_text}")


# Виклик основної функції
main()