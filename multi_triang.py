import turtle
def draw_triang(some_turtle,initlen,layer):
    len=initlen/layer
    for i in range(1,4):
        some_turtle.forward(len)
        some_turtle.left(120)


def draw_multitriang():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.color("red")
    brad.speed(0.5)
    initlen=300
    layer=1
    draw_triang(brad,initlen,layer)
    layer=layer+1
    brad.forward(initlen/layer)
    brad.left(60)
    draw_triang(brad,initlen,layer)
#    for layer in range(1,3):
    
    window.exitonclick()


def draw_k():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.color("red")
    brad.shape("turtle")
    brad.speed(1)
    brad.right(90)
    brad.forward(200)
    brad.left(180)
    brad.forward(100)
    brad.right(60)
    brad.forward(100)
    brad.left(180)
    brad.forward(100)
    brad.left(120)
    brad.forward(100)

    window.exitonclick()

draw_k()