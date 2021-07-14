import turtle


class pen(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.color("black")

    def write_country(self, data_about_country, cor_x_country, cor_y_country):
        self.goto(x=cor_x_country, y=cor_y_country)
        self.write(arg=data_about_country, move=False, align="center", font=("Arial", 12, "normal"))
