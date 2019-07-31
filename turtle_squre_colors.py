import turtle

backgroundColor = "white"

listOfColors = [
    "red",
    "purple",
    "blue",
    "green",
    "orange",
    "yellow",
    "pink",
    "gold",
    "medium spring green",
    "medium violet red"
]
tutrtleSpeed = 102

window = turtle.getscreen()
window.bgcolor(backgroundColor)



turtleCircle = turtle.Turtle()
turtleCircle.shape("turtle")


turtleCircle.speed(tutrtleSpeed)
turtleCircle.pensize(2)

steps = 300
colorIdx = 0
linesColor = listOfColors[colorIdx]
turtleCircle.color(linesColor)
# for loop
for i in range(1,1342):
    if i % 4 == 0:
        angle += 3
    else:
        angle = 90

    turtleCircle.forward(steps)
    turtleCircle.left(angle)
    if i % 4 == 0:
        colorIdx += 1
        linesColor = listOfColors[colorIdx % len(listOfColors)]
        turtleCircle.color(linesColor)


window.exitonclick()
