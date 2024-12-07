def print_colored_text(text):
    reset = "\033[0m"
    green = "\033[32m"
    print(f"{green}{text}{reset}")

# 1
print_colored_text("task --> 1")

def is_year_leap(year):
    # Перевірка, чи є рік високосним
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# 2
print_colored_text("task --> 2")

def is_year_leap(year):
    # Перевірка, чи є рік високосним
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    # Список з кількістю днів у кожному місяці
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Перевірка на коректність аргументів
    if month < 1 or month > 12:
        return None

    # Перевірка, чи є рік високосним
    if month == 2 and is_year_leap(year):
        return 29

    # Повернення кількості днів у місяці
    return days_in_months[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "-> ", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# 3
print_colored_text("task --> 3")

def is_year_leap(year):
    # Перевірка, чи є рік високосним
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    # Список з кількістю днів у кожному місяці
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Перевірка на коректність аргументів
    if month < 1 or month > 12:
        return None

    # Перевірка, чи є рік високосним
    if month == 2 and is_year_leap(year):
        return 29

    # Повернення кількості днів у місяці
    return days_in_months[month - 1]

def day_of_year(year, month, day):
    # Перевірка на коректність аргументів
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None

    # Обчислення дня року
    day_of_year = 0
    for m in range(1, month):
        day_of_year += days_in_month(year, m)
    day_of_year += day

    return day_of_year

# Тестуючий код
test_data = [
    (2000, 12, 31),
    (2001, 2, 28),
    (2004, 2, 29),
    (2023, 13, 1),  # Некоректний місяць
    (2023, 2, 30),  # Некоректний день
    (2023, 1, 1),
    (2023, 12, 31)
]
test_results = [366, 59, 60, None, None, 1, 365]

for i in range(len(test_data)):
    year, month, day = test_data[i]
    print(year, month, day, "-> ", end="")
    result = day_of_year(year, month, day)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# 4
print_colored_text("task --> 4")

def is_prime(num):
    # Перевірка, чи число менше або дорівнює 1
    if num <= 1:
        return False
    # Перевірка, чи число ділиться на будь-яке число від 2 до квадратного кореня числа
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

# 5
print_colored_text("task --> 5")

# Константи для перетворень
miles_in_km = 1.609344
gallons_in_liter = 3.785411784

def liters_100km_to_miles_gallon(liters):
    # Розрахунок
    miles_per_100km = 100 / miles_in_km  # 100 км у милях
    gallons = liters / gallons_in_liter  # Літри у галони

    return miles_per_100km / gallons

def miles_gallon_to_liters_100km(miles):
    # Розрахунок
    km_per_mile = miles_in_km  # Мілі в кілометрах
    liters_per_mile = gallons_in_liter / km_per_mile  # Літри на милю

    return 100 * liters_per_mile / miles

# Тестуючий код
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

# 6
print_colored_text("task --> 6")

def is_a_triangle(a, b, c):
    # Перевіряємо умови існування трикутника
    return a + b > c and a + c > b and b + c > a

# Тести
print(is_a_triangle(3, 4, 5))  # Очікується: True
print(is_a_triangle(1, 10, 12))  # Очікується: False
print(is_a_triangle(7, 7, 7))  # Очікується: True
print(is_a_triangle(0, 2, 2))  # Очікується: False

# 7
print_colored_text("task --> 7")

def is_a_triangle(a, b, c):
    # Перевіряємо умови існування трикутника
    return a + b > c and a + c > b and b + c > a

def is_a_right_triangle(a, b, c):
    # Перевіряємо, чи є трикутник
    if not is_a_triangle(a, b, c):
        return False

    # Перевіряємо теорему Піфагора
    sides = sorted([a, b, c])  # Впорядковуємо сторони за зростанням
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Тести
print(is_a_right_triangle(3, 4, 5))  # Очікується: True (прямокутний)
print(is_a_right_triangle(6, 8, 10))  # Очікується: True (прямокутний)
print(is_a_right_triangle(1, 2, 3))  # Очікується: False (не трикутник)
print(is_a_right_triangle(5, 5, 5))  # Очікується: False (рівносторонній, але не прямокутний)
