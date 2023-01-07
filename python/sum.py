# Программа складывает натуральные числа от 10 до n
# sum = 10+n

nat = int(input("Введите n: "))
sum = 0
i = 10

while i <= nat:
    print("i=", i)
    sum = sum + i
    i = i + 0.01
    # if sum > 100:
    #     break
else:
    print("Цикл закончился")

print("Сумма чисел от 10 до n =", sum)
