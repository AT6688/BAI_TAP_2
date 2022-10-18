import turtle

turtle.pensize(5)
turtle.pencolor("blue")

#mat ngoai

facesize = 200
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.circle(facesize)

#ve mat

turtle.fillcolor("red")
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()

#khai bao bien size cua mat

eyesize = 17.5

turtle.begin_fill()
turtle.circle(eyesize)
turtle.end_fill()

turtle.penup()
turtle.goto(100,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eyesize)
turtle.end_fill()

#ve mui
turtle.penup ()
turtle.goto(0,50)
turtle.pendown()
turtle.circle(-70, steps=3)

#ve mieng
turtle.penup()
turtle.goto(-100, -70)
turtle.pendown()
turtle.right(90)
turtle.circle(100,180)
turtle.mainloop()

turtle.done()
