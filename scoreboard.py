import turtle as t
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'bold')


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0

    def show_scoreboard(self):
        self.goto(0, 275)
        self.write(arg=f'Score: {self.score}', move=True, align=ALIGNMENT, font=FONT)

    def add_one(self):
        self.score += 1
        self.clear()
        self.show_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'GAME OVER', move=True, align=ALIGNMENT, font=FONT)