user_str = input("Введите число 0..9: ")
if user_str == "0":
    print("Нуль")
elif user_str == "1":
    print("Один")
elif user_str == "2":
    print("Два")
elif user_str == "3":
    print("Три")
elif user_str == "4":
    print("Четыре")
elif user_str == "5":
    print("Пять")
elif user_str == "6":
    print("Шесть")
elif user_str == "7":
    print("Семь")
elif user_str == "8":
    print("Восемь")
elif user_str == "9":
    print("Девять")


number_lst = [
    "Нуль",
    "Один",
    "Два",
    "Три",
    "Четыре",
    "Пять",
    "Шесть",
    "Семь",
    "Восемь",
    "Девять",
]
print(number_lst[int(user_str)])

number_dct = {
    "0": "Нуль",
    "1": "Один",
    "2": "Два",
    "3": "Три",
    "4": "Четыре",
    "5": "Пять",
    "6": "Шесть",
    "7": "Семь",
    "8": "Восемь",
    "9": "Девять",
}
print(number_dct[user_str])

# number_dct = dict(zip([str(x) for x in range(0, 9)], number_lst))
