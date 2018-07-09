import turtle


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

# Create the turtle Angie which draws a circlular fractal
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(0.4)
    for i in range(1, 37):
        angie.right(10)
        angie.circle(100)
    window.exitonclick()
draw_art()
