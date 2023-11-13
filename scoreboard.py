from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score : {0}", False, "center", ("Arial", 9, "normal"))

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", False, "center", ("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER : Your Score {self.score}", False, "center", ("Arial", 20, "normal"))
