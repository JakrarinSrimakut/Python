import turtle
import math
import random
import winsound

#set up the sceen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invader")
wn.bgpic("C:/Users/Jack/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/Games/Space_Invader/SpaceInvaderBackground/space_invaders_background.gif")

#Paths to files
invader_gif_path = "C:/Users/Jack/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/Games/Space_Invader/Player/player.gif"
player_gif_path = "C:/Users/Jack/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/Games/Space_Invader/Invader/invader.gif"
laser_wav_path = "C:/Users/Jack/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/Games/Space_Invader/laser.wav"
explosion_wav_path = "C:/Users/Jack/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/Games/Space_Invader/explosion.wav"


#Register the shapes
turtle.register_shape(invader_gif_path)
turtle.register_shape(player_gif_path)

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0
#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Ariel", 14, "normal"))

#create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape(player_gif_path)
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Choose a number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #Create te enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
#create the enemy
    enemy.color("red")
    enemy.shape(invader_gif_path)
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2


#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x <= -280:   #boundery checking for player
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x >= 280:
        x = 280
    player.setx(x)

def fire_bullet():
    if not bullet.isvisible():
        winsound.PlaySound(laser_wav_path, winsound.SND_ASYNC)
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

#As player gets more points increase enemy speed. Use class for enemy to contain enemyspeed
def calcEnemySpeed():
    global enemyspeed
    if score == 10 and enemyspeed == 2:
        enemyspeed = 3
        print("enemyspeed:{}".format(enemyspeed))
        return enemyspeed
    elif score == 20 and enemyspeed == 3:
        enemyspeed = 4
        print("enemyspeed:{}".format(enemyspeed))
        return enemyspeed
    else:
        return enemyspeed

#Create keyboard bndings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main game loop
while True:
    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        #enemyspeed = calcEnemySpeed(enemyspeed)
        x += calcEnemySpeed() #TODO replace enemyspeed with func calcEnemySpeed()
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor() > 280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #Move all enemies down
            for e in enemies: 
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1

        #Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound(explosion_wav_path, winsound.SND_ASYNC)
            #Reset the bullet
            bullet.hideturtle()
            bullet.setposition(0, -400) #move bullet offscreen so enemy don't run to invisible bullet
            #Reset the enemy    
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear() #Clear so score don't stack on previous
            score_pen.write(scorestring, False, align="left", font=("Ariel", 14, "normal"))

        if isCollision(player, enemy):
            winsound.PlaySound(explosion_wav_path, winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Move the bullet
    if bullet.isvisible():
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check o see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()


wn.mainloop()