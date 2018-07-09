import turtle
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.color("red")
    brad.speed(0.2)
    total_count=60
    turn_angle=360/total_count
    for i in range(1,total_count+1):
        draw_square(brad)
        brad.right(turn_angle)
    window.exitonclick()


draw_art()