import random

print('Добро пожаловать в числовую угадайку!')

a = random.randint(1, 100)

def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100

c = 0

n = input("Угадай число от 1 до 100: ")

while not is_valid(n):
    n = input("Некорректный ввод. Попробуй ещё раз: ")

n = int(n)

while True:
    c += 1
    if n == a:
        print(f"С {c} попытки! Молодец!")
        break
    elif n > a:
        n = input("Слишком МНОГО, попробуй ещё: ")
    else:
        n = input("Слишком МАЛО, попробуй ещё: ")

    while not is_valid(n):
        n = input("Некорректный ввод. Попробуй ещё раз: ")

    n = int(n)
