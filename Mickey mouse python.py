import turtle

bg = turtle.Screen()
bg.bgcolor("silver")

turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(1)

def draw_circle(turtle, color, size, x,y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    
draw_circle(turtle,"black", 80, 0,-60)
draw_circle(turtle,"black", 45, 60, 60)
draw_circle(turtle,"black", 45,-60, 60)
