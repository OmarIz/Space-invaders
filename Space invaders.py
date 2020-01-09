import turtle 
import time 
import random
start = False
seconds = 1
n = 4
nb = 4
nc = 4
score = 0000
shieldsize = 37
shieldsizeb = 35
shieldsizec = 35
def stopstart():
    global start 
    start = True

screen = turtle.Screen()
screen.title("Space invaders")
screen.setup(width = 800, height = 600)
screen.bgcolor("black")

gun = turtle.Turtle()
gun.speed(0) 
gun.penup() 
gun.shape("triangle")
gun.color("white")
gun.goto(0,-280)
gun.left(90)

bullet = turtle.Turtle() 
bullet.speed(0)
bullet.penup()
bullet.shape("square")
bullet.color("red")
bullet.goto(gun.xcor(),-250)
bullet.shapesize(stretch_wid= 1, stretch_len = 0.1)
bullet.hideturtle()
bullet.dy= 0

shield = turtle.Turtle() 
shield.speed(0)
shield.penup()
shield.shape("square")
shield.color("blue")
shield.goto(0,-160)
shield.shapesize(stretch_wid = 1, stretch_len = 4.65116279)

shield_b = turtle.Turtle() 
shield_b.speed(0)
shield_b.penup()
shield_b.shape("square")
shield_b.color("blue")
shield_b.goto(300,-160)
shield_b.shapesize(stretch_wid = 1, stretch_len = 4)

shield_c = turtle.Turtle() 
shield_c.speed(0)
shield_c.penup()
shield_c.shape("square")
shield_c.color("blue")
shield_c.goto(-300,-160)
shield_c.shapesize(stretch_wid = 1, stretch_len = 4)

alien = turtle.Turtle() 
alien.speed(0)
alien.penup()
alien.shape("circle")
alien.color("green")
alien.goto(0,100)
alien.dx = 2
alien.dy = 0

alien_bullet = turtle.Turtle() 
alien_bullet.speed(0)
alien_bullet.penup()
alien_bullet.shape("square")
alien_bullet.color("purple")
alien_bullet.goto(2000,2000)
alien_bullet.shapesize(stretch_wid= 1, stretch_len = 0.1)
alien_bullet.hideturtle()
alien_bullet.dy= 0

right_checker = turtle.Turtle()
right_checker.speed(0)
right_checker.penup()
right_checker.shape("circle")
right_checker.goto(200,0)
right_checker.dx = 1.5
right_checker.dy = 0
right_checker.hideturtle()

left_checker = turtle.Turtle()
left_checker.speed(0)
left_checker.penup()
left_checker.shape("circle")
left_checker.goto(-200,0)
left_checker.dx = 1
left_checker.dy = 0
left_checker.hideturtle()

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.color("white")
pen.goto(0,200)
pen.write("Score: {} ".format(score), align="center",font=("OCR A Extended", 24 ,"bold"))

startpen = turtle.Turtle()
startpen.hideturtle()
startpen.speed(0)
startpen.penup()
startpen.color("white")
startpen.goto(0,0)
startpen.write("Press 'w' to start", align="center",font=("OCR A Extended", 24 ,"bold"))

endpen = turtle.Turtle()
endpen.hideturtle()
endpen.speed(0)
endpen.penup()
endpen.color("white")
endpen.goto(0,0)


aliena = turtle.Turtle() 
aliena.speed(0)
aliena.penup()
aliena.shape("circle")
aliena.color("green")
aliena.goto(-50,100)

alienb = turtle.Turtle() 
alienb.speed(0)
alienb.penup()
alienb.shape("circle")
alienb.color("green")
alienb.goto(50,100)




def gun_left(): 
    x = gun.xcor()
    x += -15 
    gun.setx(x)

def gun_right(): 
    x = gun.xcor()
    x += +15 
    gun.setx(x)

    

def shoot():
    startpen.clear()
    stopstart()
    if bullet.ycor() > 300: 
        bullet.dy = 0
        bullet.hideturtle()
        bullet.goto(gun.xcor(),-250)
    bullet.showturtle()
    bullet.dy = 10
    y = bullet.ycor() 
    y += bullet.dy 
    bullet.sety(y) 

screen.listen()
screen.onkeypress(shoot, 'w')
screen.onkeypress(gun_left, 'a')
screen.onkeypress(gun_right, 'd')

def alienshoot():
    alien_bullet.showturtle()
    alien_bullet.dy = 10
    y = alien_bullet.ycor() 
    y += alien_bullet.dy 
    alien_bullet.sety(y)

while start == False: 
    bullet.goto(gun.xcor(),-250)

while True:
    screen.update()

    bullet.sety(bullet.ycor() + bullet.dy)
    right_checker.setx(right_checker.xcor() + alien.dx)
    left_checker.setx(left_checker.xcor() + alien.dx)
    alien.setx(alien.xcor() + alien.dx)
    aliena.setx(aliena.xcor() + alien.dx)
    alienb.setx(alienb.xcor() + alien.dx)
    alien_bullet.sety(alien_bullet.ycor() - alien_bullet.dy)

    if gun.xcor() > 365:
        gun.setx(365)
    
    if gun.xcor() < -365:
        gun.setx(-365)

    if alien_bullet.ycor() < -300: 
        alien_bullet.dy = 0
        alien_bullet.goto(2000,2000)

    if alien_bullet.xcor() == 2000:
        if alien_bullet.ycor() == 2000:
            shooter = random.randint(1,3)
            dead = shooter
            while shooter == dead:
                shooter = random.randint(1,3)
                if shooter == 1: 
                    if alien.xcor() > 1000:
                        dead = 1
                    elif alien. xcor() < 800:
                        alien_bullet.goto(alien.xcor(),alien.ycor() - 20)
                        alienshoot()
                        dead = 0
                if shooter == 2: 
                    if aliena.xcor() > 1000:
                        dead = 2
                    elif aliena.xcor() < 800:
                        alien_bullet.goto(aliena.xcor(),aliena.ycor() - 20)
                        alienshoot()
                        dead = 0
                if shooter == 3: 
                    if alienb.xcor() > 1000:
                        dead = 1
                    elif alienb.xcor() < 800:
                        alien_bullet.goto(alienb.xcor(),alienb.ycor() - 20)
                        alienshoot()
                        dead = 0
    
    if right_checker.xcor() > 340:
        if alien.dx < 30:
            alien.dy = 10 
            alien.sety(alien.ycor() - alien.dy)
            aliena.sety(aliena.ycor() - alien.dy)
            alienb.sety(alienb.ycor() - alien.dy)
            alien.dx *= -1.2
            alien.dy = 0
        elif alien.dx >= 30:
            alien.dy = 10
            alien.sety(alien.ycor() - alien.dy)
            aliena.sety(aliena.ycor() - alien.dy)
            alienb.sety(alienb.ycor() - alien.dy)
            alien.dx = -30
            
    
    if left_checker.xcor() < -340:
        if alien.dx > -30:
            alien.dy = 10
            alien.sety(alien.ycor() - alien.dy)
            aliena.sety(aliena.ycor() - alien.dy)
            alienb.sety(alienb.ycor() - alien.dy)
            alien.dx *= -1.2
            alien.dy = 0
        elif alien.dx <= -30:
            alien.dy = 10
            alien.sety(alien.ycor() - alien.dy)
            aliena.sety(aliena.ycor() - alien.dy)
            alienb.sety(alienb.ycor() - alien.dy)
            alien.dx = 30
            alien.dy = 0
            


    if shield.xcor() - shieldsize < bullet.xcor() < shield.xcor() + shieldsize: 
        if bullet.ycor() == shield.ycor() - 20:
            bullet.hideturtle()
            bullet.goto(0,350)
            n = n * 0.86
            if n > 1:
                shield.shapesize(stretch_wid = 1, stretch_len = n)
                shieldsize += -2
            elif n < 1: 
                shield.goto(2000,2000)
    
    if shield.xcor() - shieldsize < alien_bullet.xcor() < shield.xcor() + shieldsize: 
        if alien_bullet.ycor() - 40 == shield.ycor() - 20:
            alien_bullet.hideturtle()
            alien_bullet.dy = 0
            alien_bullet.goto(2000,2000)
            n = n * 0.86
            if n > 1:
                shield.shapesize(stretch_wid = 1, stretch_len = n)
                shieldsize += -2
            elif n < 1: 
                shield.goto(2000,2000)
    
    if shield_c.xcor() - shieldsizec < bullet.xcor() < shield_c.xcor() + shieldsizec: 
        if bullet.ycor() == shield_c.ycor() - 20:
            bullet.hideturtle()
            bullet.goto(0,350)
            nc = nc * 0.86
            if nc > 1:
                shield_c.shapesize(stretch_wid = 1, stretch_len = nc)
                shieldsizec += -2
            elif nc < 1: 
                shield_c.goto(2000,2000)
    
    if shield_c.xcor() - shieldsizec < alien_bullet.xcor() < shield_c.xcor() + shieldsizec: 
        if alien_bullet.ycor() - 40 == shield_c.ycor() - 20:
            alien_bullet.hideturtle()
            alien_bullet.dy = 0
            alien_bullet.goto(2000,2000)
            n = n * 0.86
            if n > 1:
                shield.shapesize(stretch_wid = 1, stretch_len = n)
                shieldsizec += -2
            elif n < 1: 
                shield_c.goto(2000,2000)
    
    if shield_b.xcor() - shieldsizeb < bullet.xcor() < shield_b.xcor() + shieldsizeb: 
        if bullet.ycor() == shield_b.ycor() - 20:
            bullet.hideturtle()
            bullet.goto(0,350)
            nb = nb * 0.86
            if nb > 1:
                shield_b.shapesize(stretch_wid = 1, stretch_len = nb)
                shieldsizeb += -2
            elif nb < 1: 
                shield_b.goto(2000,2000)
    
    if shield_b.xcor() - shieldsizeb < alien_bullet.xcor() < shield_b.xcor() + shieldsizeb: 
        if alien_bullet.ycor() - 40 == shield_b.ycor() - 20:
            alien_bullet.hideturtle()
            alien_bullet.dy = 0
            alien_bullet.goto(2000,2000)
            nb = nb * 0.86
            if nb > 1:
                shield_b.shapesize(stretch_wid = 1, stretch_len = nb)
                shieldsizeb += -2
            elif nb < 1: 
                shield.goto(2000,2000)
    
    if gun.xcor() -20 < alien_bullet.xcor() < gun.xcor() +20:
        if gun.ycor() - 20 < alien_bullet.ycor() < gun.ycor() + 20:
            endpen.write("GAMEOVER", align="center",font=("OCR A Extended", 24 ,"bold"))
            alien.dx = 0
            alien.dy = 0 
            left_checker.dx = 0 
            right_checker.dx = 0
            bullet.dy = 0 
            x = 0 
            alien_bullet.dy = 0
    
    if alien_bullet.xcor() - 5 < bullet.xcor() < alien_bullet.xcor() + 5: 
        if alien_bullet.ycor() - 20 < bullet.ycor() < alien_bullet.ycor() + 20:
            score += 10
            pen.clear()
            pen.write("Score: {} ".format(score),align="center" ,font=("OCR A Extended", 24 ,"bold"))
            alien_bullet.dy = 0
            bullet.dy = 0 
            alien_bullet.goto(2000,2000)
            bullet.goto(0,350)
    
    if alien.ycor() == gun.ycor():
        endpen.write("GAMEOVER", align="center",font=("OCR A Extended", 24 ,"bold"))
        alien.dx = 0
        alien.dy = 0 
        left_checker.dx = 0 
        right_checker.dx = 0
        bullet.dy = 0 
        x = 0 
        alien_bullet.dy = 0
 

    
    if alien.xcor() - 20 < bullet.xcor() < alien.xcor() + 20: 
        if alien.ycor() - 20 < bullet.ycor() < alien.ycor() + 20:
            score += 100
            pen.clear()
            pen.write("Score: {} ".format(score),align="center" ,font=("OCR A Extended", 24 ,"bold"))
            alien.goto(2000,2000)
            bullet.dy = 0
            bullet.hideturtle()
            bullet.goto(0,350)
            alien.hideturtle()
    
    if aliena.xcor() - 20 < bullet.xcor() < aliena.xcor() + 20: 
        if aliena.ycor() - 20 < bullet.ycor() < aliena.ycor() + 20:
            score += 100
            pen.clear()
            pen.write("Score: {} ".format(score),align="center" ,font=("OCR A Extended", 24 ,"bold"))
            aliena.goto(2000,2000)
            bullet.dy = 0
            bullet.hideturtle()
            bullet.goto(0,350)
            aliena.hideturtle()
    
    if alienb.xcor() - 20 < bullet.xcor() < alienb.xcor() + 20: 
        if alienb.ycor() - 20 < bullet.ycor() < alienb.ycor() + 20:
            score += 100
            pen.clear()
            pen.write("Score: {} ".format(score),align="center" ,font=("OCR A Extended", 24 ,"bold"))
            alienb.goto(2000,2000)
            bullet.dy = 0
            bullet.hideturtle()
            bullet.goto(0,350)
            alienb.hideturtle()

  

    

   
