word = input("Введите слово: ").lower()
mistake = 0
print("Загадано слово из " + str(len(word)) + " букв. Ваш ход.")
correct_char = ""
while True:
    j = 0
    show_word = ""
    while j < len(word):
        if word[j].lower() in correct_char:
            show_word += word[j].lower()
        else:
            show_word += "_"
        j += 1
    print(show_word)
    print("Число ошибок: ", mistake)
    if "_" not in show_word:
        print("Вы победили!")
        break

    char = input("Введите букву: ").lower()
    if len(char) != 1:
        break
    if char in word.lower() and char not in correct_char:
        correct_char += char
    else:
        mistake += 1

    if mistake > 10:
        print("Вы проиграли!")
        break
