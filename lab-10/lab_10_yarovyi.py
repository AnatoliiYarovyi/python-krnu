def print_colored_text(text):
    reset = "\033[0m"
    green = "\033[32m"
    print(f"{green}{text}{reset}")

# 1
print_colored_text("task --> 1")


def is_hidden(word, combination):
    """Перевіряє, чи символи першого рядка приховані у другому."""
    word = word.lower()
    combination = combination.lower()
    start_index = 0

    for char in word:
        # Знаходимо позицію символу у combination, починаючи з start_index
        start_index = combination.find(char, start_index)
        if start_index == -1:  # Якщо символ не знайдено
            return False
        start_index += 1  # Переміщуємо індекс далі

    return True


# Використання
word = input("Введіть слово: ")
combination = input("Введіть комбінацію символів: ")

if is_hidden(word, combination):
    print(f"Слово '{word}' приховане у комбінації '{combination}'.")
else:
    print(f"Слово '{word}' НЕ приховане у комбінації '{combination}'.")

# 2
print_colored_text("task --> 2")

def calculate_life_number():
    while True:
        try:
            date = input("Введіть дату народження у форматі YYYYMMDD: ")
            if len(date) != 8 or not date.isdigit():
                raise ValueError("Некоректний формат дати. Введіть дату у форматі YYYYMMDD.")

            while True:
                sum = 0
                for symbol in date:
                    sum += int(symbol)

                date = str(sum)

                if len(date) == 1:
                    break

            print("Число життя:", sum)
            break

        except ValueError as e:
            print(e)
            print("Спробуйте ще раз.")

calculate_life_number()

# 3
print_colored_text("task --> 3")

def get_valid_input(prompt, lower_bound, upper_bound):
    while True:
        try:
            value = int(input(prompt))
            if lower_bound <= value <= upper_bound:
                return value
            else:
                print(f"Error: wrong input --> число повинно бути в діапазоні ({lower_bound}..{upper_bound})")
        except ValueError:
            print("Error: wrong input")

# Приклад використання функції
lower_bound = 1
upper_bound = 10
prompt = f"Введіть ціле число в діапазоні від {lower_bound} до {upper_bound}: "

result = get_valid_input(prompt, lower_bound, upper_bound)
print("Введене значення:", result)


