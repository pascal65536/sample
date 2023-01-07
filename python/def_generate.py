def generate(count=10):
    import random

    i = 0
    random_lst = list()
    while i < count:
        random_lst.append(random.randint(0, 100))
        i += 1
    return random_lst


ret = generate()
print(ret)
ret = generate(20)
print(ret)
