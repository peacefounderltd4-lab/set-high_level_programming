@staticmethod
def draw(list_rectangles, list_squares):
    """Open a window and draw all rectangles and squares."""
    import turtle

    screen = turtle.Screen()
    screen.title("Rectangles and Squares")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)

    def draw_shape(x, y, width, height, color):
        pen.penup()
        pen.goto(x, y)
        pen.setheading(0)
        pen.pendown()

        pen.fillcolor(color)
        pen.begin_fill()

        for _ in range(2):
            pen.forward(width)
            pen.right(90)
            pen.forward(height)
            pen.right(90)

        pen.end_fill()

    for rectangle in list_rectangles:
        draw_shape(
            rectangle.x,
            rectangle.y,
            rectangle.width,
            rectangle.height,
            "skyblue"
        )

    for square in list_squares:
        draw_shape(
            square.x,
            square.y,
            square.width,
            square.height,
            "lightgreen"
        )

    pen.hideturtle()
    turtle.done()
