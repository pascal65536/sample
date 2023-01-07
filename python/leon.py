import random

secret = random.randint(0, 100)
counter = 0

while True:
    counter = counter + 1
    num = input("Введите число от 0 до 100: ")
    if not num.isdigit():
        print("Это не число")
    elif int(num) > secret:
        print("Перелёт")
    elif int(num) < secret:
        print("Недолёт")
    elif int(num) == secret:
        print("Попал!")
        break

print("Игра окончена", counter, "Попыток")
