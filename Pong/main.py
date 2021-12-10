import turtle
import os
import winsound

#Initialize
gme = turtle.Screen()
gme.title("PONG")
gme.bgcolor("black")
gme.setup(width = 700, height = 600)

#Ball
ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.dx = 4
ball.dy = 4

#Player1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.shapesize(stretch_wid = 4, stretch_len = .5)
p1.color("Green")
p1.penup()
p1.goto(-300, 0)

#Player2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.shapesize(stretch_wid = 4, stretch_len = .5)
p2.color("Red")
p2.penup()
p2.goto(300, 0)

#Controls
def p1_up():
    y = p1.ycor()
    y += 15
    p1.sety(y)
    
def p1_down():
    y = p1.ycor()
    y -= 15
    p1.sety(y)
    
def p2_up():
    y = p2.ycor()
    y += 15
    p2.sety(y)
    
def p2_down():
    y = p2.ycor()
    y -= 15
    p2.sety(y)
    
#Ball Movement
def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
#KeyBindings
gme.listen()
gme.onkeypress(p1_up, "w")
gme.onkeypress(p1_down, "s")
gme.onkeypress(p2_up, "Up")
gme.onkeypress(p2_down, "Down")

#P1ScoreDisplay
p1_score_display = turtle.Turtle()
p1_score_display.speed(0)
p1_score_display.color("Green")
p1_score = 0
p1_score_display.penup()
p1_score_display.hideturtle()
p1_score_display.goto(-200, 250)
p1_score_display._write("Player 1: " + str(p1_score), align = "center", font = ("arial", 16, "normal"))

#P2ScoreDisplay
p2_score_display = turtle.Turtle()
p2_score_display.speed(0)
p2_score_display.color("Red")
p2_score = 0
p2_score_display.penup()
p2_score_display.hideturtle()
p2_score_display.goto(200, 250)
p2_score_display._write("Player 2: " + str(p2_score), align = "center", font = ("arial", 16, "normal"))

#Main Game Loop
while True:
    gme.update()
    move_ball()
    
    #bounce off ceiling and floor
    if ball.ycor() > 295:
        #os.system("aplay boop.wav&")
        #os.system("afplay boop.wav&")
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)
        ball.sety(295)
        ball.dy *= -1
    elif ball.ycor() < -295:
        #os.system("aplay boop.wav&")
        #os.system("afplay boop.wav&")
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)
        ball.sety(-295)
        ball.dy *= -1
    
    #reset & increment score if ball goes off either edge
    if ball.xcor() > 340:
        ball.goto(0, 0)
        ball.dx *= -1
        p1_score += 1
        p1_score_display.clear()
        p1_score_display._write("Player 1: " + str(p1_score), align = "center", font = ("arial", 16, "normal"))
    elif ball.xcor() < -340:
        ball.goto(0, 0)
        ball.dx *= -1
        p2_score += 1
        p2_score_display.clear()
        p2_score_display._write("Player 2: " + str(p2_score), align = "center", font = ("arial", 16, "normal"))
        
    #bounce off paddles
    if (ball.xcor() < -280) and (ball.ycor() < p1.ycor() + 50 and ball.ycor() > p1.ycor() - 50) :
        #os.system("aplay boop.wav&")
        #os.system("afplay boop.wav&")
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)
        ball.setx(-280)
        ball.dx *= -1
    elif (ball.xcor() > 280) and (ball.ycor() < p2.ycor() + 50 and ball.ycor() > p2.ycor() - 50):
        #os.system("aplay boop.wav&")
        #os.system("afplay boop.wav&")
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)
        ball.setx(280)
        ball.dx *= -1
    
    