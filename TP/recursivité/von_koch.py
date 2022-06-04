import turtle

height = 400
width = 400
turtle.screensize(canvwidth=width, canvheight=height, bg="black")
t = turtle.Turtle()
t.speed(0)
t.pencolor("yellow")
t.penup()
t.sety(height/2)
t.pendown()

def koch (n, longueur):
    if n==0:
        t.forward(longueur)
    else:
        koch(n-1, longueur/3)
        t.left(60)
        koch(n-1, longueur/3)
        t.right(120)
        koch(n-1, longueur/3)
        t.left(60)
        koch(n-1, longueur/3)
        


for i in range(3):
    koch(1, 3**5)
    t.right(120)


a = input("Fermer la fenêtre\n")
if a:
    turtle.bye()
