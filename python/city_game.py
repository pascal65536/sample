# Игра "города"

char_start = 'а'
while True:
    answer = 'Введите название города, вам на "' + char_start + '": '
    word = input(answer)
    if len(word) == 0:
        print('Конец игры')
        break
    elif word[0] == char_start:
        char_start = word[-1]
    else:
        print('Не правильно')
