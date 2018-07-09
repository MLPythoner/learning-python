#Coded by Ramnik

import turtle

window = turtle.Screen()
window.bgcolor("white")

abc =turtle.Turtle()
abc.shape("arrow")
abc.color("black")
abc.speed(6)

#for alphabet R
abc.pu()
abc.setpos(-50,0)
abc.pd()
abc.left(90)
abc.forward(100)
abc.right(90)
abc.seth(0)
abc.circle(50,180)
abc.left(90)
abc.forward(100)
abc.setpos(0,0)

#for alphabet A
abc.pu()
abc.setpos(10,0)
abc.pd()
abc.seth(0)
abc.left(75)
abc.forward(200)
abc.right(150)
abc.forward(200)
x = abc.xcor()
print(x)
abc.right(180)
abc.forward(80)
abc.seth(180)
abc.forward(62)

#for alphabet M
abc.pu()
abc.setpos(x+10,0)
abc.pd()
abc.seth(90)
abc.forward(200)
abc.right(165)
abc.forward(150)
abc.left(150)
abc.forward(150)
abc.seth(270)
abc.forward(200)


# code for flower design
abc.shape("classic")
abc.color("blue")
abc.speed(8)

abc.pu()
abc.setpos(-200,0)
abc.pd()

for i in range(1,40):  
    abc.left(35)
    abc.forward(50)
    abc.right(35)
    abc.forward(50)
    abc.right(145)
    abc.forward(50)
    abc.right(35)
    abc.forward(50)
    abc.right(10)
abc.seth(270)
abc.forward(200)
        

window.exitonclick()