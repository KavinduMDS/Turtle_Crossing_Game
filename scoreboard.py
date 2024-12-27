from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score =0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220,250)
        self.write(f"LEVEL: {self.score}", align="center", font= ("Courier", 24, "normal"))

    def score_increase(self):
        self.score+=1

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 24, "normal"))
