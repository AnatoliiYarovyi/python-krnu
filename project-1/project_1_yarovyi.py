from random import randrange

def display_board(board):
    """Відображає поточний стан дошки."""
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|   " + "   |   ".join(row) + "   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    """Запитує користувача про його хід і оновлює дошку."""
    while True:
        try:
            move = int(input("Ваш хід (виберіть число 1-9): "))
            if move < 1 or move > 9:
                raise ValueError
            row, col = divmod(move - 1, 3)
            if board[row][col] not in 'XO':
                board[row][col] = 'O'
                break
            else:
                print("Це поле вже зайняте!")
        except ValueError:
            print("Некоректний вибір. Спробуйте ще раз.")

def make_list_of_free_fields(board):
    """Повертає список усіх вільних полів."""
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in 'XO':
                free.append((row, col))
    return free

# def victory_for(board, sign):
#     """Перевіряє, чи є перемога для заданого символу."""
#     # Перевіряємо рядки та стовпці
#     for i in range(3):
#         if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
#             return True
#     # Перевіряємо діагоналі
#     if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
#         return True
#     return False

def victory_for(board, sign):
    """Перевіряє, чи є перемога для заданого символу."""
    # Визначаємо всі можливі виграшні комбінації
    winning_combinations = [
        # Рядки
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Стовпці
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Діагоналі
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    # Перевіряємо, чи кожна виграшна комбінація заповнена одним знаком
    for combination in winning_combinations:
        if all(board[row][col] == sign for row, col in combination):
            return True
    return False

def draw_move(board):
    """Робить хід комп'ютера та оновлює дошку."""
    free = make_list_of_free_fields(board)
    if free:
        move = free[randrange(len(free))]
        board[move[0]][move[1]] = 'X'

# Ініціалізація дошки
board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
board[1][1] = 'X'  # Комп'ютер починає з центру

# Основний ігровий цикл
while True:
    display_board(board)
    if victory_for(board, 'X'):
        print("Комп'ютер виграв!")
        break
    if not make_list_of_free_fields(board):
        print("Нічия!")
        break
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("Ви виграли!")
        break
    if not make_list_of_free_fields(board):
        print("Нічия!")
        break
    draw_move(board)