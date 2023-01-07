"""
Вася составляет 4-буквенные коды из букв У, Л, Е, Й. 
Каждую букву нужно использовать ровно 1 раз,
при этом код не может начинаться с буквы Й и не может содержать сочетания ЕУ. 
Сколько различных кодов может составить Вася?
"""

from itertools import product
p=product('УЛЕЙ', repeat=4)
k=0
for word in p:
    s=' '.join(word)
    if (s.count('У') == 1) and (s.count('Л') == 1) and \
       (s.count('Е') == 1) and (s.count('Й') == 1) and \
       (s[0]!='Й') and (s.find('ЕУ')==-1):
        k+=1
print(k)
