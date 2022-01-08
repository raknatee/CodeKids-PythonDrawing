from turtle import penup, goto, pendown, color, begin_fill, end_fill


def logo(points, start_point, object_color):
    penup()
    goto(start_point)
    pendown()
    color(object_color)
    
    begin_fill()

    for i in range(len(points)):
        x, y = points[i]
        goto(x, y)

    end_fill()
