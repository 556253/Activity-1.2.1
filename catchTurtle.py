# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
turtle_shape = "circle"
turtle_color = "pink"
turtle_size = 2
score = 0
timer = 30
counter_interval = 1000
timer_up = False

#-----initialize turtle-----
painter = trtl.Turtle()
score_writer = trtl.Turtle()
counter = trtl.Turtle()
painter.color(turtle_color)
painter.shape(turtle_shape)
painter.turtlesize(turtle_size)
painter.penup()
painter.speed(0)
score_writer.speed(0)
score_writer.penup()
score_writer.goto(-300, 270)
score_writer.hideturtle()
counter.speed(0)
counter.penup()
counter.goto(-300, 250)
counter.hideturtle()
font_setup = ("jay da bay", 20, "normal")

#-----game functions--------
def painter_clicked(x, y):
    if(timer_up == False):    
        painter.showturtle()
        painter.turtlesize(rand.randrange(1, 4))
        trtl.Screen().bgcolor(rand.random(), rand.random(), rand.random())
        painter.fillcolor(rand.random(), rand.random(), rand.random())
        update_score()
        change_position()
    else:
        painter.hideturtle()
def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    painter.goto(new_xpos, new_ypos)
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
painter.onclick(painter_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()