def age_movie(age):
    if age < 14:
        print("Нет")
    else:
        print("Да")


def age_movie(age):
    age = input("Ваш возраст")
    age = int(age)
    if age < 14:
        print("Вы слишком молоды")
    elif age > 60:
        print("Вам лучше прогуляться возле дом")
    else:
        print("Да, можете попытаться покорить Эльбрус")


def age_elbrus(age):
    result = True
    if age < 14:
        result = False
    elif age > 60:
        result = False
    else:
        result = True
    return result


def is_triangle(a, b, c):

    if a > b and a > c:
        max_len_side = a
        len_two_side = b + c
    if b > a and b > c:
        max_len_side = b
        len_two_side = a + c
    if c > a and c > b:
        max_len_side = c
        len_two_side = a + b

    return len_two_side > max_len_side


if __name__ == "__main__":
    print("d" * 80)
    # a + b + c - a < a
    # a + b + c - b < b
    # a + b + c - c < c
