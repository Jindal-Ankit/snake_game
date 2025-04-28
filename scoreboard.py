from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(-10, 280)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score = {self.score}",
                   move=False,
                   align="right",
                   font=("Arial", 15, "normal"))

    def increse_score(self):
        self.score +=1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!", move=False, align="center", font=("Arial", 20, "normal"))


