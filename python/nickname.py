import random

vowel = 'aeiouy'  # гласные
consonant = 'bcdfghjklmnpqrstvwxz'  # согласные
i = 0
while i < 10:
    name = ''
    j = 0
    while j < 3:
        name += random.choice(consonant)
        name += random.choice(vowel)
        j += 1 
    print(name.capitalize())    
    i += 1
