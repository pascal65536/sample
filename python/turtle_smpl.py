from turtle import *
from random import *


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

i = 0
while i < 10000:
    v = randint(0, 2)
    my_dot = (
        my_dot[0] - (my_dot[0] + dot_lst[v][0]) / 2,
        my_dot[1] - (my_dot[1] + dot_lst[v][1]) / 2,
    )
    goto(my_dot)
    dot()

    i += 1

done()
