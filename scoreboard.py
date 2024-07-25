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
        with open('highscore.txt', 'r') as file:
            self.high_score = int(file.read())
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.goto(0, 275)
        self.write(arg=f'Score: {self.score} High Score {self.high_score}', move=True, align=ALIGNMENT, font=FONT)

    def add_one(self):
        self.score += 1
        self.show_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.show_scoreboard()

