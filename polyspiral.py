# encoding: utf-8

import turtle as t
from random import randint

WIDTH = 800
HEIGHT = 800

def spiral(distance, angle, increment, segments):
    # by default, a pyturtle faces east
    t.left(0)
    for i in range(1, segments+1):
        t.forward(distance * (0.6 * WIDTH))
        try:
            # angle = angle * (1 / random.randint(-2, 2))
            angle += (1 / randint(-2, 2))
        except ZeroDivisionError:
            angle += 1
        t.pensize(randint(1, 10))
        t.right(angle)
        distance += increment
# spiral(0.01, 89.5, 0.01, 184)
spiral(0.01, 90, 0.01, 184)
