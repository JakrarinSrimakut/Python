import turtle
import winsound

class Game:
    def __init__(self, game_runs, winning_score, winner):
        self.game_runs = game_runs #Check if game keeps running
        self.winning_score = winning_score
        self.winner = winner
        self.game_over_pen = turtle.Turtle()

    def display_game_over(self):
        self.game_over_pen.speed(0)
        self.game_over_pen.color("white")
        self.game_over_pen.penup()
        self.game_over_pen.hideturtle()
        self.game_over_pen.goto(0, 0)
        self.game_over_pen.write("Game Over\nThe winner is {}\nEnter:Play again Esc:Exit!!".format(winner), align="center", font=("Courier", 20, "bold"))


    def undisplay_game_over(self):
        self.game_over_pen.clear()
        self.game_runs = True

pong_game = Game(True, 3, "")

wn = turtle.Screen()
wn.title("Pong by @Shrimpnugget")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #make game run without auto update so it's faster

# sound file path
bounce_wav_path = "C:/Users/Jack/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/Games/Pong/bounce.wav"

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() #turtle is module, Turtle() is class
paddle_a.speed(0) # set spd of animation max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # stop turtle drawing line while moving
paddle_a.goto(-350, 0) # start at this location


# Paddle B
paddle_b = turtle.Turtle() #turtle is module, Turtle() is class
paddle_b.speed(0) # set spd of animation max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # stop turtle drawing line while moving
paddle_b.goto(350, 0) # start at this location

# Ball
ball = turtle.Turtle() #turtle is module, Turtle() is class
ball.speed(0) # set spd of animation max
ball.shape("square")
ball.color("white")
ball.penup() # stop turtle drawing line while moving
ball.goto(0, 0) # start at this location
ball.dx = .2 # dx,dy change
ball.dy = -.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor() #return y coordinate
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor() #return y coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #return y coordinate
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor() #return y coordinate
    y -= 20
    paddle_b.sety(y)

#TODO allow user to press enter in window to restart game not in terminal
# def continue_game():
#     if(not pong_game.game_runs):
#         pong_game.game_runs = True
#         pong_game.undisplay_game_over()

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") 
wn.onkeypress(paddle_b_down, "Down")
#wn.onkeypress(continue_game, "Return")

# Main game loop
while True:
    print("game runs:{}".format(pong_game.game_runs))

    while pong_game.game_runs:
        wn.update()


        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking ball
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound(bounce_wav_path, winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound(bounce_wav_path, winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # Border checking paddles
        if paddle_a.ycor() > 250:
            paddle_a.sety(250)

        if paddle_a.ycor() <-250:
            paddle_a.sety(-250)

        if paddle_b.ycor() > 250:
            paddle_b.sety(250)

        if paddle_b.ycor() <-250:
            paddle_b.sety(-250)

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound(bounce_wav_path, winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350)and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound(bounce_wav_path, winsound.SND_ASYNC)

        # End game
        if ((score_a or score_b) == pong_game.winning_score):
            if(score_a == pong_game.winning_score):
                winner = "Player A"
            elif(score_b == pong_game.winning_score):
                winner = "Player B"
            score_a = 0
            score_b = 0
            pong_game.game_runs = False
    
    # Show game over screen
    if(not pong_game.game_runs):
        pong_game.display_game_over()
        input("Press enter to continue...")
        pong_game.undisplay_game_over()