import turtle as t


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0

    def show_scoreboard(self):
        self.goto(0, 275)
        self.write(arg=f'Score: {self.score}', move=True, align='center', font=('Arial', 16, 'bold'))

    def add_one(self):
        self.score += 1
        self.show_scoreboard()

