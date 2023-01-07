import random

s2 = random.randint(1, 10)
solution = random.randint(1, 20)
s1 = solution * s2

print(s1, s2, solution)

res = input("Сколько будет " + str(s1) + "/" + str(s2) + "? ")


if not res.isdigit():
    print("Надо ввести ответ цифрами")
elif int(res) == solution:
    print("Правильно!")
else:
    print("Не правильно ((")
