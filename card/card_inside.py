import turtle


class InternalCard:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(900, 900)
        self.turtle_text = turtle.Turtle()
        self.turtle_text.hideturtle()
        self.font_style = ('Courier', 30, "normal")
        self.turtle_text.penup()

    def _initialise(self):
        # want to pen up so we don't draw a line moving the turtle to text block
        self.turtle_text.speed('fastest')
        self.turtle_text.setpos(0, 350)
        self.turtle_text.color('black')

    def top_insider(self, user):
        self._initialise()
        self.turtle_text.pendown()
        if user:
            self.turtle_text.write(f'Dear {user}', font=self.font_style, align='center')
        else:
            self.turtle_text.write('Dear User', font=self.font_style, align='center')
        self.turtle_text.penup()
        # turtle.done()

    def middle_insider(self):
        self.turtle_text.setpos(0, 30)
        self.turtle_text.pendown()
        self.turtle_text.write('Happy Holidays!', font=self.font_style, align='center')
        self.turtle_text.penup()
        self.turtle_text.setpos(0, 0)
        self.turtle_text.pendown()
        self.turtle_text.write('Fingers crossed next year is better', font=self.font_style, align='center')
        self.turtle_text.penup()

    def lower_insider(self):
        self.turtle_text.setpos(0, -350)
        self.turtle_text.pendown()
        self.turtle_text.write('From', font=self.font_style, align='center')
        self.turtle_text.penup()
        self.turtle_text.setpos(0, -380)
        self.turtle_text.pendown()
        self.turtle_text.write('The IDS Team', font=self.font_style, align='center')
        self.turtle_text.penup()

    def build_internal(self, user):
        self.top_insider(user)
        self.middle_insider()
        self.lower_insider()
        turtle.exitonclick()
