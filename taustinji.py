import turtle
turtle.setup(500, 500) #maina loga izmēru
screen=turtle.Screen()  #izveido logu, bet nav nenodzēšams kursors 0,0 koordinātēs
screen.bgcolor("gray")
t=turtle.Turtle("turtle")
t.speed(-1)  #pārvietošanās momentāla


def moveForward():
    t.forward(10)
def moveBackward():
    t.backward(10)
def moveRight():
    t.right(30)
    moveForward()
def moveLeft():
    t.left(30)
    moveForward()


screen.onkey(moveForward, "Up")  #nospiežot pogu (šajā gadījumā bultiņu uz augšu) pārvietosies uz priekšu
screen.onkey(moveLeft, "Left")
screen.onkey(moveRight,"Right")
screen.onkey(moveBackward, "Down")


screen.onkeypress(moveForward, "Up")
screen.onkeypress(moveLeft, "Left")
screen.onkeypress(moveRight,"Right")
screen.onkeypress(moveBackward, "Down")

#onkey- nospiežot
#onkeypress- turot
#onkeyrelease- atlaižot

def mouseDragging(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(mouseDragging)


def clearScreen(x,y):
    t.clear()
t.ondrag(mouseDragging)
screen.onclick(clearScreen, 3)


screen.listen()
screen.mainloop()