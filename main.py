import turtle
wn = turtle.Screen()
ground = turtle.Turtle()
# makes turtle invisible and sets speed
ground.hideturtle()
ground.speed(0)
# takes turtle to starting position
ground.penup()
ground.goto(-400,-200)
ground.pendown()
# makes ground color green
ground.pencolor("green")
ground.fillcolor("green")
# makes ground
ground.begin_fill()
for i in range(2):
  ground.forward(600)
  ground.left(90)
  ground.forward(100)
  ground.left(90)
ground.end_fill()

# imports sky turtle
sky = turtle.Turtle()
# makes turtle invisible and sets speed
sky.hideturtle()
sky.speed(0)
# brings turtle to starting position
sky.penup()
sky.goto(-400,-100)
sky.pendown()
# sets sky color
sky.pencolor("deepskyblue")
sky.fillcolor("deepskyblue")
# makes sky rectangle
sky.begin_fill()
for i in range(2):
  sky.forward(600)
  sky.left(90)
  sky.forward(300)
  sky.left(90)
sky.end_fill()

def bouncing():
  ball.speed(0)
  ball.setheading(90)
# imports ball and makes it circular
ball = turtle.Turtle()
ball.shape("circle")
# hides ball, turns off trail, and moves it to starting position
ball.speed(0)
ball.hideturtle()
ball.penup()
ball.goto(150,150)
ball.showturtle()
# drops ball
ball.speed(7)
ball.goto(140,-95)
# variable x position of bounces
x_pos = 65
while(x_pos > 0):
  bouncing()
  ball.speed(5)
  ball.circle(x_pos,180)
  if x_pos > 20:
    ball.speed(3)
  x_pos = x_pos - 5
  
#draw ball trail
trail = turtle.Turtle()
y_pos = -200
while(y_pos == -200):
  ball.pendown()
  ball.begin_fill()
  ball.fillcolor("black")
  ball.circle(x_pos, y_pos)
  ball.end_fill()
  ball.penup()