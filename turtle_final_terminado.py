import turtle

turtle.getscreen()

turtle.shape("turtle")

turtle.shapesize(2,2,2)

turtle.fillcolor("purple")

turtle.color("white","purple")

color = turtle.Screen()

color.bgcolor("black")

turtle.speed(9)

turtle.pensize()
turtle.pensize(3)

turtle.begin_fill()

for i in range(8):
    turtle.forward(200)

    turtle.left(135)


turtle.end_fill()

turtle.hideturtle()

turtle.exitonclick()