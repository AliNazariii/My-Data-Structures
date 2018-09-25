import turtle


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    for j in range(0, 30):
        for i in range(0, 4):
            brad.forward(100)
            brad.right(90)
        brad.right(12)

    window.exitonclick()


draw_shapes()
