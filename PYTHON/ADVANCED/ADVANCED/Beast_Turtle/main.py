import turtle
X=-10
Y=220
canvas=turtle.Screen()
artist=turtle.Turtle()
canvas.setup(1200,1000)
canvas.bgcolor("Black")
artist.speed(0)
artist.penup()
artist.goto(X,Y)
artist.goto(X,Y)
artist.pendown()
artist.hideturtle()

colors = [
    "cyan",
    "deepskyblue", # loop1
    "blue",
    "mediumblue",
    "purple",      
    "magenta"
]

colours=[ "white","Cyan","deepskyblue","violet"] #loop4


bolors = [
    "white",    #loop #2
    "cyan",
    "magenta",
    "white"
]

satellites = [
    "cyan",      #loop #3
    "magenta"
]


artist.penup()
artist.goto(X,Y)
artist.setheading(0)
artist.pendown()



# PORTAL

for i in range(300):
    artist.color(colors[i % 6])
    artist.forward(i)
    artist.left(59)
    artist.width((i % 2))


# BASE 1

for s in range(8):

    artist.penup()
    artist.goto(X,Y)

    artist.setheading(90 + (s * 45))
    artist.forward(180)

    artist.color(bolors[s % 4])
    artist.width(4)

    artist.pendown()

    artist.setheading(90 + (s * 45))

    artist.forward(80)

    artist.backward(40)

    artist.left(30)
    artist.forward(35)

    artist.backward(35)

    artist.right(60)
    artist.forward(35)

    artist.backward(35)

#3

artist.penup()
artist.goto(X, Y)
artist.setheading(90)

for j in range(8):

    artist.penup()
    artist.goto(X, Y)

    artist.setheading(90 + (j * 45))
    artist.forward(230)

    artist.left(30)

    artist.pendown()
    artist.color(satellites[j % 2])
    artist.width(2)

    for m in range(3):
        artist.forward(70)
        artist.right(120)

#tringular blaster
artist.penup()
artist.goto(X,Y)
artist.setheading(0)
artist.pendown()


for k in range(255):

    artist.color(colours[k % 4])
    artist.width((k % 3) + 1)

    for l in range(3):
        artist.forward(k)
        artist.right(120)

    artist.right(3) 
    
for p in range(60):

    if p % 3 == 0:

        artist.penup()
        artist.goto(X,Y)

        artist.setheading(p * 6)

        artist.forward(320 + (p % 4) * 5)

        artist.color(bolors[p % 4])

        artist.pendown()

        artist.forward(5)
        

artist.penup()
artist.goto(-500,400)
artist.color(colors[5])
artist.write("CREDITS : AQUS-AIE",
             font=("Ariel", 14, "Bold")
            )
    
    
        
