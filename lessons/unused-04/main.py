from shin_chan import (
    ankur,
    allLegs,
    myShirt,
    myHead,
    allHands,
    myMouth,
    allEyebrows,
    allEyes,
    myRobot,
)
from turtle import hideturtle, done, Screen, speed, pensize


def main():
    # initial
    s = Screen()
    s.screensize(700, 1000)
    s.bgcolor("orange")
    speed(5)
    pensize(2)
    hideturtle()
    # start drawing
    ankur()
    allLegs()
    myShirt()
    myHead()
    allHands()
    myMouth()
    allEyebrows()
    allEyes()
    myRobot()
    # end drawing
    # for allow window to stay up
    done()


main()
