def print_colored_text(text):
    reset = "\033[0m"
    green = "\033[32m"
    print(f"{green}{text}{reset}")


# 1
print_colored_text("task --> 1")
import math

def gaussian(x, mu, sigma):
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    return coefficient * math.exp(exponent)

def get_float_input(message):
        value = float(input(message))
        return value

# Запитуємо у користувача значення для mu, sigma і x
mu = get_float_input("Введіть значення mu (середнє значення): ")
sigma = get_float_input("Введіть значення sigma (стандартне відхилення): ")
x = get_float_input("Введіть значення x: ")

# Обчислюємо значення функції Гауса
result = gaussian(x, mu, sigma)

# Виводимо результат
print(f"Значення функції Гауса для x={x}, mu={mu}, sigma={sigma} дорівнює {result}")

# 1-1
print_colored_text("task --> 1-1")
mu = 1
sigma = 2
x = 3

exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
result = coefficient * math.exp(exponent)
print(f"Значення функції Гауса для x={x}, mu={mu}, sigma={sigma} дорівнює {result}")

# 2
print_colored_text("task --> 2")
john = 3
mary = 5
adam = 6
print(f"{john}, {mary}, {adam}")

totalApple = john + mary + adam
print(totalApple)
print("Всього яблук:", totalApple)

# 3
print_colored_text("task --> 3")
kilometers = 12.25
miles = 7.38

coefficient = 1.61

miles_to_kilometers = miles * coefficient
kilometers_to_miles = kilometers / coefficient

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# 4
print_colored_text("task --> 4")
x = input("Введіть значення х")
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3**x - 1
print("y =", y)

# 5
print_colored_text("task --> 5")
# this program computes the number of seconds in a given number of hours
hours = 3
secondsInHour = 3600

print(f"Seconds in {hours} Hour(s): ", hours * secondsInHour)
print("Goodbye")

# 6
print_colored_text("task --> 6")
a = float(input("Введіть значення a"))
b = float(input("Введіть значення b"))

# result of addition
print(a + b)
# result of subtraction
print(a - b)
# result of multiplication
print(a * b)
# result of division
print(a / b)

print("\nThat's all, folks!")

# 7
print_colored_text("task --> 7")
x = float(input("Enter value for x: "))

def evaluate_expression(x, depth):
    if depth == 0:
        return x
    else:
        return 1 / (x + evaluate_expression(x, depth - 1))

# Глибина рекурсії для виразу
depth = 5

# Обчислення виразу
y = evaluate_expression(x, depth)

print("y =", y)

# 8
print_colored_text("task --> 8")
start_hour = int(input("Starting time (hours): "))
start_minute = int(input("Starting time (minutes): "))
duration_minutes = int(input("Event duration (minutes): "))

def calculate_end_time(start_hour, start_minute, duration_minutes):
    # Обчислюємо загальну кількість хвилин від початку доби (00:00) до початку події
    total_minutes = start_hour * 60 + start_minute

    # Додаємо тривалість події в хвилинах
    total_minutes += duration_minutes

    # Обчислюємо кінцевий час
    end_hour = total_minutes // 60
    end_minute = total_minutes % 60

    # Якщо кінцевий час перевищує 24 години, зменшуємо його на 24 години
    end_hour %= 24

    # Виводимо результат
    print(f"Подія закінчується о {end_hour:02}:{end_minute:02}")

calculate_end_time(start_hour, start_minute, duration_minutes)

