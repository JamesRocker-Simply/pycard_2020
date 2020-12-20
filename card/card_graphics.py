import turtle
import random


def make_ball(x, y, size, colour, ball):
    ball.hideturtle()
    ball.penup()
    ball.setposition(x, y)
    ball.color(colour)
    ball.dot(size)
    print(ball.position())


class Card:
    def __init__(self):
        #  setup the screen to 900 by 900 and two turtles for the circle baubles and squares for tree
        self.screen = turtle.Screen()
        self.screen.bgcolor("#02053b")
        self.screen.setup(900, 900)
        self.star = turtle.Turtle()
        self.turtle_text = turtle.Turtle()
        self.turtle_text.hideturtle()  # we want to initialise the turtle but hide it for later
        self.snow_size = 7
        self.list_of_snow = []

    def move_snow(self, snow):
        snow_speed = 2
        position = snow.position()
        snow.clear()
        x_axis = position[0]
        y_axis = position[1] - snow_speed
        make_ball(x_axis, y_axis, self.snow_size, "white", snow)

    def let_it_snow(self):
        rate_of_snow_balls = 2
        rand_make_snow = random.randint(0, rate_of_snow_balls)
        width = 900

        if rand_make_snow == 0:
            snow = turtle.Turtle()  # initialise a snowball
            snow.hideturtle()
            snow.penup()
            self.list_of_snow.append(snow)  # make a list of snowballs
            make_ball(random.randint(int(-width / 2), int(width / 2)), width / 2, self.snow_size, "white", snow)

        for snow in self.list_of_snow:
            self.move_snow(snow)
            if snow.position()[1] <= -width / 2:  # This is so when the snow meets the half way it disappears
                snow.clear()
                self.list_of_snow.remove(snow)
                del snow

        self.screen.update()

    def build_star(self):
        self.star.color('yellow')
        self.star.speed('fastest')
        self.star.setpos(60, 0)
        self.star.hideturtle()
        self.star.begin_fill()
        angle = 144
        size = 200
        self.star.begin_fill()

        for side in range(5):
            self.star.forward(size)
            self.star.right(angle)
            self.star.forward(size)
            self.star.right(72 - angle)
        self.star.end_fill()

    def build_cover(self):
        self.build_star()
        font_style = ("Elephant", 30, "bold")
        self.turtle_text.penup()  # want to pen up so we don't draw a line moving the turtle to text block

        # configs
        self.turtle_text.speed('fastest')
        self.turtle_text.setpos(0, 350)
        self.turtle_text.color('red')
        self.turtle_text.pendown()
        self.turtle_text.write('Holiday Wishes', font=font_style, align='center')
        self.turtle_text.hideturtle()

        self.screen.tracer(0)
        for _ in range(25):
            self.let_it_snow()
        for _ in range(25):
            self.let_it_snow()
        for _ in range(500):
            self.let_it_snow()

        turtle.clear()
        turtle.clearscreen()
