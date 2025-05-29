import turtle

t = turtle.Turtle()

t.goto(100, 0)
t.color("pink")

for i in range(5):
    t.forward(100)
    t.left(72)

turtle.exitonclick()

# Creating and Setting
t = turtle.Turtle()
t.setheading( direction )

# Moving
t.goto( -300 , 25 )
t.forward( 10 )
t.left( 45 )
t.right( 90 )
t.speed( 10 )

# Drawing
t.penup()
t.pendown()
t.begin_fill()
t.end_fill()
# Color
t.color( "pink" )
turtle.Screen().bgcolor("orange")


# Rotating Shape
for i in range( n ):
    t.forward( distance )
    t.left( inside_angle + 1)

# Growing Shape
for i in range( n ):
    t.forward( distance + i)
    t.left( angle )

# Color Changing Shape
colors = ["pink","cyan","gray"]
for i in range( n ):
    t.color( colors[ i % 3 ] )
    t.forward( distance)
    t.left( angle )
