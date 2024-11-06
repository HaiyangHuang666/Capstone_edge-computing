from turtle import *

def draw_bus():
    # Set up the turtle
    speed(5)
    bgcolor("white")
    pensize(3)
    color("black")

    # Draw the body of the bus
    penup()
    goto(-150, -50)
    pendown()
    begin_fill()
    fillcolor("gold")  # Change the color of the bus body as desired

    # Draw the main rectangular body of the bus
    forward(300)  # Bottom line
    left(90)
    forward(100)  # Right side
    left(90)
    forward(273)  # Top line
    left(60)
    forward(58)
    left(30)
    forward(50)  # Left side
    left(90)

    end_fill()

    # Draw the windows of the bus
    window_color = "lightblue"
    penup()
    goto(-120, 0)
    pendown()
    for _ in range(5):
        begin_fill()
        fillcolor(window_color)
        forward(40)
        left(90)
        forward(30)
        left(90)
        forward(40)
        left(90)
        forward(30)
        left(90)
        end_fill()
        penup()
        forward(50)
        pendown()

    # Draw the wheels
    # Left wheel
    penup()
    goto(-90, -80)
    pendown()
    begin_fill()
    fillcolor("black")
    circle(20)
    end_fill()

    # Right wheel
    penup()
    goto(90, -80)
    pendown()
    begin_fill()
    fillcolor("black")
    circle(20)
    end_fill()

    # Add the label "HKU Shuttle Bus"
    penup()
    goto(-70, -40)
    pendown()
    color("black")
    write("HKU Shuttle Bus", font=("Arial", 16, "bold"))

    # Hide the turtle and finish
    penup()
    goto(0, -150)
    done()

# Run the function to draw the bus
draw_bus()