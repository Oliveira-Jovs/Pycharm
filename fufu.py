from turtle import *

no_of_spins=0
def spin_the_fidget():
    global no_of_spins
    #clearing the objects on the turtle window
    clear()
    #setting the angle based on number of spins
    angle = no_of_spins / 10
    dot(120, 'black')
    #setting the angle
    right(angle)
    #Drawing the first lobe
    #Moving the mouse by 100 units in the 'angle' direction to draw the arm
    forward(150)
    dot(120, 'red') #Drawing the cap at the end of the arm of radius 120 units and red color
    back(150) #Moving the drawing pen back to the center
    #Drawing the second lobe
    right(120) #Changing the angle  to right by 120 degrees
    #Moving the mouse by 100 units in the 'angle' direction to draw the second arm
    forward(150)
    dot(120, 'green')#Drawing the cap at the end of the arm of radius 120 units and green color
    back(150)#Moving the drawing pen back to the center
    #Drawing the third lobe
    right(120)#Changing the angle  to right by 120 degrees
    #Moving the mouse by 100 units in the 'angle' direction to draw the third arm
    forward(150)
    dot(120, 'blue')#Drawing the cap at the end of the arm of radius 120 units and blue color
    back(150)#Moving the drawing pen back to the center
    right(120)#Changing the angle  to right by 120 degrees
    update() #Updating the turtle window


def draw_spinner():
    global no_of_spins
    #Decreasing the number of spins by 1 after rotating the spinner once
    if no_of_spins > 0:
        no_of_spins -= 1

    spin_the_fidget() #Drawing the spinner on window
    ontimer(draw_spinner, 20) #Updating the window regularly


def flipSpinner():
    global no_of_spins
    #Increasing the number of spins by 10 on pressing the space button
    no_of_spins += 10


def gameWin():
    #width,height,startx,starty
    setup(450, 450, 370, 50)
    hideturtle() #hiding the turtle symbol
    tracer(False) #offing the turtle animations
    title("PythonGeeks Fidget Spinner Game")
    width(20) #setting the width
    onkey(flipSpinner, 'space') #running the flipSpinner function on pressing space button
    listen() #listening to the keyboard press
    draw_spinner() #Updating the spinner on window
    done()

setup(420, 420, 370, 50)
hideturtle() #hiding the turtle symbol
tracer(False) #offing the turtle animations
title("PythonGeeks Fidget Spinner Game")
setposition(-170, 180)
write("PythonGeeks Fidget Spinner Game", font=("Calibre",15, "bold"))
setposition(0, 0)
write("Press the Space button to \nstart the game", font=("Calibre",15, "normal"),align='center')
onkey(gameWin, 'space') #running the flipSpinner function on pressing space button
listen()
done()