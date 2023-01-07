from turtle import *
from random import *
import math

# http://grep.cs.msu.ru/python3.8_RU/digitology.tech/docs/python_3/library/turtle.html


hex_str = "0123456789abcdef"


def to_hex(lft, rt):
    ret = int(math.sqrt((lft[0] - rt[0]) ** 2 + (lft[1] - rt[1]) ** 2) / 600 * 256)
    return hex_str[ret // 16] + hex_str[ret % 16]


clear()
penup()
speed(0)
dot_lst = list()
dot_lst.append((-300, -200))
dot_lst.append((300, -200))
dot_lst.append((0, 200))
for i in range(0, 3):
    goto(dot_lst[i])
    dot()

my_dot = (0, 0)
goto(my_dot)
dot()

color_lst = ["red", "green", "blue"]
i = 0
max_aa = 0
max_bb = 0
max_cc = 0
while i < 10000:
    v = randint(0, 2)
    rr = to_hex(my_dot, dot_lst[0])
    gg = to_hex(my_dot, dot_lst[1])
    bb = to_hex(my_dot, dot_lst[2])
    col = f"#{rr}{gg}{bb}"
    if len(col) < 7:
        print(rr, gg, bb)
    pencolor(col)
    # pencolor()

    my_dot = (
        dot_lst[v][0] + (my_dot[0] - dot_lst[v][0]) / 2,
        dot_lst[v][1] + (my_dot[1] - dot_lst[v][1]) / 2,
    )
    goto(my_dot)
    dot()

    i += 1

done()
