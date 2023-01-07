# Проверка числа на простоту. Поиск натуральных делителей

import time

num = int(input("Enter number: "))
max_divizors = num // 2
is_prime = False
start_time = time.time()
while max_divizors > 1:
    if not num % max_divizors:
        print(max_divizors)
        is_prime = True
    max_divizors -= 1

print(time.time() - start_time)
print(num, is_prime)
