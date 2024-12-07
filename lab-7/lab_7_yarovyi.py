def print_colored_text(text):
    reset = "\033[0m"
    green = "\033[32m"
    print(f"{green}{text}{reset}")

# 1
print_colored_text("task --> 1")

# Створення списку чисел
numbers_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Конвертація списку у кортеж
numbers_tuple = tuple(numbers_list)

# Запит користувача ввести число n
n = int(input("Введіть число n: "))

# Створення порожнього списку result
result = []

# Проходження по кортежу та додавання чисел, які менші за n, до списку result
for num in numbers_tuple:
    if num < n:
        result.append(num)

# Виведення чисел з нового списку result
print("Числа, які менші за", n, ":", result)

# 2
print_colored_text("task --> 2")

# Створення кортежу з трьох елементів, які є рядками
my_tuple = ("apple", "banana", "cherry")

# З'єднання елементів кортежу в один рядок з комою як роздільником
result = ", ".join(my_tuple)

# Виведення результату
print(result)

# 3
print_colored_text("task --> 3")

# Створення словника з інформацією про книги
library = {
    "1984": {"author": "George Orwell", "year": 1949, "pages": 328},
    "To Kill a Mockingbird": {"author": "Harper Lee", "year": 1960, "pages": 281},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925, "pages": 218},
    "Pride and Prejudice": {"author": "Jane Austen", "year": 1813, "pages": 432},
    "Moby-Dick": {"author": "Herman Melville", "year": 1851, "pages": 635}
}

# Запит користувача ввести назву книги
book_title = input("Введіть назву книги: ")

# Виведення інформації про книгу, якщо вона існує в бібліотеці
if book_title in library:
    book_info = library[book_title]
    print(f"Інформація про книгу '{book_title}':")
    print(f"Автор: {book_info['author']}")
    print(f"Рік видання: {book_info['year']}")
    print(f"Кількість сторінок: {book_info['pages']}")
else:
    print(f"Книга '{book_title}' не знайдена в бібліотеці.")

# 4
print_colored_text("task --> 4")

# Створення словника з інформацією про студентів
students = {
    "Doe": ("John", 20, 85.5),
    "Smith": ("Jane", 22, 90.0),
    "Brown": ("Emily", 21, 88.0),
    "Johnson": ("Michael", 23, 87.5),
    "Williams": ("Sarah", 24, 92.0)
}

# Запит користувача ввести прізвище студента
last_name = input("Введіть прізвище студента: ")

# Виведення інформації про студента, якщо він існує в словнику
if last_name in students:
    student_info = students[last_name]
    print(f"Інформація про студента '{last_name}':")
    print(f"Ім'я: {student_info[0]}")
    print(f"Вік: {student_info[1]}")
    print(f"Середній бал: {student_info[2]}")
else:
    print(f"Студент з прізвищем '{last_name}' не знайдений.")

# 5
print_colored_text("task --> 5")

# Телефонна книга
phone_book = {
    "John Doe": ["+123456789", "+987654321"],
    "Jane Smith": ["+1122334455"],
    "Alice Johnson": ["+1222333444", "+1444333222"],
}

# Функція для додавання нового номера телефону до контакту
def add_phone_number(contact_name, phone_number):
    if contact_name in phone_book:
        phone_book[contact_name].append(phone_number)
    else:
        phone_book[contact_name] = [phone_number]

# Додаємо нові номери телефонів
add_phone_number("John Doe", "+112345678")
add_phone_number("New Contact", "+1999888777")

# Виводимо список номерів телефонів для всіх контактів
for contact, numbers in phone_book.items():
    print(f"{contact}: {', '.join(numbers)}")

