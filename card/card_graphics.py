import turtle
import time


class Card:
    def __init__(self):
        #  setup the screen to 900 by 900 and two turtles for the circle baubles and squares for tree
        self.screen = turtle.Screen()
        self.screen.setup(900, 900)
        self.circle = turtle.Turtle()
        self.square = turtle.Turtle()
        self.turtle_text = turtle.Turtle()
        self.turtle_text.hideturtle()  # we want to initialise the turtle but hide it for later
        self.position = 0
        self.font_style = ('Courier', 30, "normal")

    def _bauble_initialise(self):
        # as the bauble is the start of the tree, we can start stamping there
        self.circle.shape('circle')
        self.circle.color('red')
        self.circle.speed('fastest')
        self.circle.up()
        self.circle.goto(0, 280)
        self.circle.stamp()

    def _foliage_initialise(self):
        self.square.shape('square')
        self.square.color('green')
        self.square.speed('fastest')
        self.square.up()

    def bauble(self, colour, each, y_axis):
        # Builds a bauble at the relative position with the passed colour
        x_axis = 30 * (each + 1)
        self.circle.color(colour)
        self.circle.goto(-x_axis, -y_axis + 280)
        self.circle.stamp()
        self.circle.goto(x_axis, -y_axis + 280)
        self.circle.stamp()

    def build_tree(self):
        self._bauble_initialise()
        self._foliage_initialise()

        for row in range(1, 17):  # 16 rows to account for the tree
            y = 30 * row  # Y axis turtle position
            each = 0  # initialise the each variable
            for each in range(row - self.position):
                x = 30 * each  # x axis turtle position
                self.square.goto(x, -y + 280)
                self.square.stamp()
                self.square.goto(-x, -y + 280)
                self.square.stamp()

            if row % 4 == 3:  # remainder of the row
                self.bauble('yellow', each, y)

            if row % 4 == 0:  # if the row cell count is divisible by 4 + 1
                self.bauble('red', each, y)
                self.position += 2  # this is so the tree comes back in on itself after the red bauble

    def build_stump(self):
        self.square.color('brown')
        # stump
        for row in range(17, 20):
            y = 30 * row
            for height in range(3):  # to calculate the stump height
                x = 30 * height
                self.square.goto(x, -y + 280)
                self.square.stamp()
                self.square.goto(-x, -y + 280)
                self.square.stamp()

    def build_cover(self, user):
        self.build_tree()
        self.build_stump()
        self.turtle_text.penup()  # want to pen up so we don't draw a line moving the turtle to text block

        # configs
        self.turtle_text.speed('fastest')
        self.turtle_text.setpos(0, 350)
        self.turtle_text.color('black')
        self.turtle_text.pendown()

        if user:
            self.turtle_text.write(f'Happy Holidays! {user}', font=self.font_style, align='center')
        else:
            self.turtle_text.write('Happy Holidays!', font=self.font_style, align='center')
        self.turtle_text.hideturtle()
        # turtle.done()
        time.sleep(5)
        turtle.clear()
        turtle.clearscreen()
