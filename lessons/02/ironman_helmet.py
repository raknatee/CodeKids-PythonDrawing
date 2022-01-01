from turtle import penup, goto, pendown, color, begin_fill, end_fill


def logo(a, b):
    penup()
    goto(b)
    pendown()
    color("#fab104")  # Light Yellow
    begin_fill()

    for i in range(len(a[0])):
        x, y = a[0][i]
        goto(x, y)

    for i in range(len(a[1])):
        x, y = a[1][i]
        goto(x, y)
    end_fill()
