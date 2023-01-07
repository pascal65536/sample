word = input("Введите слово: ").lower()
mistake = 0
print("Загадано слово из " + str(len(word)) + " букв. Ваш ход.")
while True:
    char = input("Введите букву: ").lower()
    if char in word:
        word = word.replace(char, ".")
        print("Есть такая буква")
    else:
        mistake += 1
        print("Нет такой буквы")

    if mistake > 10:
        break

    if "." * len(word) == word:
        print("Это победа!")
        break

print(word)
