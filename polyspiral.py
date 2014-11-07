# encoding: utf-8

import turtle as t


WIDTH = 800
HEIGHT = 800


def spiral(distance, angle, increment, segments):
    # by default, a pyturtle faces east
    t.left(0)
    for i in range(1, segments+1):
        t.forward(distance * (0.6 * WIDTH))
        t.right(angle)
        distance += increment

spiral(0.01, 89.5, 0.01, 184)
