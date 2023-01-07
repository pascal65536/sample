import random

i = 0
count = 0
success = 0
while i < 10:
    s2 = random.randint(1, 10)
    sol = random.randint(1, 20)
    s1 = sol * s2

    res = input("Сколько будет " + str(s1) + " / " + str(s2) + " = ")
    count += 1
    if not res.isdigit():
        print("Нужно вводить только цифры")
    elif sol == int(res):
        print("Правильно!")
        success += 1
    else:
        print("Вы ошиблись")
    i += 1

print("Вы правильно ответили на", success, "вопросов из", count)
