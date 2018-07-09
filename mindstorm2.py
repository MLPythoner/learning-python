
import turtle
def draw_triang(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.left(120)

def draw_diamond(some_turtle):
    some_turtle.right(30)
    some_turtle.forward(100)
    some_turtle.left(60)
    some_turtle.forward(100)
    some_turtle.left(120)
    some_turtle.forward(100)
    some_turtle.left(60)
    some_turtle.forward(100)
    some_turtle.left(150)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.color("red")
    brad.speed(0.5)
    total_count=60
    turn_angle=360/total_count
    for i in range(1,total_count+1):
        draw_diamond(brad)
        brad.left(turn_angle)
    window.exitonclick()


draw_art()