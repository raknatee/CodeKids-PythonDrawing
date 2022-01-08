from turtle import screensize, pensize, speed, done
from doraemon import Doraemon


def main():
    # initial
    screensize(800, 600, "#f0f0f0")
    pensize(3)
    speed(9)
    # start drawing
    Doraemon()
    # end drawing
    # for allow window to stay up
    done()


main()
