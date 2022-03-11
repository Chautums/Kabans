import turtle
wn=turtle.Screen()
wn.title("Pingpong")
wn.bgcolor("black")
wn.setup(800, 600)
wn.tracer(0)

#Siena A
siena_a=turtle.Turtle()
siena_a.speed(0)
siena_a.shape("square")
siena_a.color("white")
siena_a.penup()
siena_a.goto(-350,0)
siena_a.shapesize(5,1)

#Siena B
siena_b=turtle.Turtle()
siena_b.speed(0)
siena_b.shape("square")
siena_b.color("white")
siena_b.penup()
siena_b.goto(350,0)
siena_b.shapesize(5,1)

#Bumba
bumba=turtle.Turtle()
bumba.speed(0)
bumba.shape("square")
bumba.color("white")
bumba.penup()
bumba.goto(0,0)
bumba.dx=2
bumba.dy=2


#Funkcijas
def siena_a_up():
    y=siena_a.ycor()
    y +=20
    siena_a.sety(y)

def siena_a_down():
    y=siena_a.ycor()
    y -=20
    siena_a.sety(y)

def siena_b_up():
    y=siena_b.ycor()
    y +=20
    siena_b.sety(y)

def siena_b_down():
    y=siena_b.ycor()
    y -=20
    siena_b.sety(y)


#Pogas
wn.listen()
wn.onkeypress(siena_a_up, "w")
wn.onkeypress(siena_a_down, "s")
wn.onkeypress(siena_b_up, "Up")
wn.onkeypress(siena_b_down, "Down")


#Loop
while True:
    wn.update()

    #Bumbas kustība
    bumba.setx(bumba.xcor() + bumba.dx)
    bumba.sety(bumba.ycor() + bumba.dy)

    #Robežas
    if bumba.ycor() > 290:
        bumba.sety(290)
        bumba.dy *= -1

    if bumba.ycor() < -290:
        bumba.sety(-290)
        bumba.dy *= -1

    if bumba.xcor() < 390:
        bumba.goto(0, 0)
        bumba.dx *= -1

    if bumba.xcor() < -390:
        bumba.goto(0, 0)
        bumba.dx *= -1


    #Siena un bumba
    if bumba.xcor() > 340 and (bumba.ycor() < siena_b.ycor() + 50)

    bam bam