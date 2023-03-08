from turtle import Turtle
class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.shape(None)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score:  {self.score}", align="center", font=("Arial", 10, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("Arial", 20, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        