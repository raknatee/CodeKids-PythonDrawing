def moon_object(obj, color, width, circle):
    obj.color(color)
    obj.width(width)
    obj.hideturtle()
    obj.begin_fill()
    obj.circle(circle)
    obj.end_fill()


def moon_movement(obj, speed):
    obj.right(speed)
    obj.forward(speed - 0.1)
