from turtle import Turtle
ALIGNMNET = "center"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as data:
            self.highscore = int(data.read())


        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game_Over", align=ALIGNMNET, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
            self.score = 0

    def increase_score(self):
        self.score += 1


    def update_score(self):
        self.clear()
        self.color("white")
        self.write(f"Score:{self.score}, High_score = {self.highscore}", align=ALIGNMNET, font=FONT)



