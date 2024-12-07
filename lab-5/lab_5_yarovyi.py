def print_colored_text(text):
    reset = "\033[0m"
    green = "\033[32m"
    print(f"{green}{text}{reset}")

# 1
print_colored_text("task --> 1")

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Введіть ціле число, щоб замінити середнє число у списку: "))

# Step 2: write a line of code that removes the last element from the list.
hat_list.pop()

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))

print(hat_list)

# 2
print_colored_text("task --> 2")

# Функція для сортування списку методом бульбашки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Інтерактивне введення елементів масива
my_list = []
n = int(input("Введіть кількість елементів у списку: "))
for i in range(n):
    element = int(input(f"Введіть елемент {i+1}: "))
    my_list.append(element)

# Сортування списку методом бульбашки
bubble_sort(my_list)

# Виведення відсортованого списку
print("Відсортований список:", my_list)

# 3
print_colored_text("task --> 3")

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Створення нового списку для унікальних елементів
unique_list = []

# Проходження через кожен елемент початкового списку
for number in my_list:
    # Якщо елемент ще не зустрічався в новому списку, додаємо його
    if number not in unique_list:
        unique_list.append(number)

# Виведення списку з унікальними елементами
print("The list with unique elements only:", unique_list)
print(my_list)

# 4
print_colored_text("task --> 4")

# Ініціалізація списку для зберігання температурних даних
temps = [[0.0 for h in range(24)] for d in range(31)]

# Припустимо, що список магічно оновлюється тут
# На приклад, ми можемо заповнити його випадковими значеннями для ілюстрації
import random
for day in temps:
    for hour in range(24):
        day[hour] = random.uniform(-10, 30)  # Випадкові температури від -10 до 30 градусів

# Обчислення середньої полуденної температури
total = 0.0

for day in temps:
    total += day[11]  # Полудень - це 12-та година (індекс 11)

average = total / 31

print("Average temperature at noon:", average)

# 5
print_colored_text("task --> 5")

# Створення матриці 8x8 з пустими клітинками
chessboard = [['_' for _ in range(8)] for _ in range(8)]

# Розташування тур по кутках шахівниці
chessboard[7][0] = 'R'  # A1
chessboard[0][0] = 'R'  # A8
chessboard[7][7] = 'R'  # H1
chessboard[0][7] = 'R'  # H8

# Виведення шахівниці
for row in chessboard:
    print(' '.join(row))