
from turtle import*


#we want to paint a house


# stap1 :draw a square

speed(15)
width(7)

color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of square

#drawing a door
begin_fill()
forward(70)
left(90)
color("yellow")
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
left(210)
forward(200)
left(120)
forward(200)
end_fill()

#Drawing windows

penup()
goto(200, 170)
pendown()
right(60)
forward(5)
color("blue")
forward(40)
left(90)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
left(90)
forward(20)
left(90)
forward(25)


penup()
goto(0, 170)
pendown()
left(90)
forward(5)
forward(40)
right(90)
forward(25)
right(90)
forward(40)
right(90)
forward(25)
right(90)
forward(20)
right(90)
forward(25)









exitonclick()



