from turtle import hideturtle, bgcolor, reset, setup, speed, title, done, tracer, update
from ironman_helmet import logo
from time import sleep

def main(bg_color, ankur_color):
    # initial
    ankur1 = [
        
            (-40, 120),
            (-70, 260),
            (-130, 230),
            (-170, 200),
            (-170, 100),
            (-160, 40),
            (-170, 10),
            (-150, -10),
            (-140, 10),
            (-40, -20),
            (0, -20),
    
            (0, -20),
            (40, -20),
            (140, 10),
            (150, -10),
            (170, 10),
            (160, 40),
            (170, 100),
            (170, 200),
            (130, 230),
            (70, 260),
            (40, 120),
            (0, 120),

    ]

    ankur2 = [
            (-40, -30),
            (-50, -40),
            (-100, -46),
            (-130, -40),
            (-176, 0),
            (-186, -30),
            (-186, -40),
            (-120, -170),
            (-110, -210),
            (-80, -230),
            (-64, -210),
            (0, -210),
     
            (0, -210),
            (64, -210),
            (80, -230),
            (110, -210),
            (120, -170),
            (186, -40),
            (186, -30),
            (176, 0),
            (130, -40),
            (100, -46),
            (50, -40),
            (40, -30),
            (0, -30),
  
    ]

    ankur3 = [
        
            (-60, -220),
            (-80, -240),
            (-110, -220),
            (-120, -250),
            (-90, -280),
            (-60, -260),
            (-30, -260),
            (-20, -250),
            (0, -250),
      
            (0, -250),
            (20, -250),
            (30, -260),
            (60, -260),
            (90, -280),
            (120, -250),
            (110, -220),
            (80, -240),
            (60, -220),
            (0, -220),
    
    ]
    hideturtle()
    bgcolor(bg_color)  # Dark Red
    setup(500, 600)
    title("I AM IRONMAN")
    ankur1Goto = (0, 120)
    ankur2Goto = (0, -30)
    ankur3Goto = (0, -220)
    speed(2)
    # start drawing
    logo(ankur1, ankur1Goto, ankur_color)
    logo(ankur2, ankur2Goto, ankur_color)
    logo(ankur3, ankur3Goto, ankur_color)
    # end drawing
    # for allow window to stay up
    

tracer(0,0)
for i in range(10):
    main("#ba161e","#fab104")
    update()
    sleep(1)
    reset()

    main("blue","pink")
    update()
    sleep(1)
    reset()
