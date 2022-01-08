# import turtle package
from turtle import (
    Screen,
    Turtle,
)

from moon import moon_movement, moon_object


def main():
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.tracer(0)
    moon = Turtle()
    crescent = Turtle()
    while True:
        moon.clear()
        moon_object(moon, "red", 100, 20)
        moon_object(crescent, "black", 100, 20)
        moon_movement(moon, 0.8)
        screen.update()


main()
