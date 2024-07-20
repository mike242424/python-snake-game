import turtle as t


class Scoreboard:

    def __init__(self):
        self.scoreboard = t.Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.color('white')
        self.scoreboard.penup()
        self.score = 0

    def show_scoreboard(self):
        self.scoreboard.goto(0, 275)
        self.scoreboard.write(arg=f'Score: {self.score}', move=True, align='center', font=('Arial', 16, 'bold'))

    def add_one(self):
        self.score += 1

