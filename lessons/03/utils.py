from turtle import (
    penup,
    goto,
    pendown,
)
def pen_up_goto_down(x, y):
    penup()
    goto(x, y)
    pendown()