def logo(pen, points, color):
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.color(color)  
    pen.begin_fill()

    for i in range(1, len(points)):
        x, y = points[i]
        pen.goto(x, y)

    pen.end_fill()
