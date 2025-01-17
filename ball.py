import turtle


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setposition(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def reset_ball(self):
        self.setposition(0, 0)
        self.bounce_x()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
