import turtle as t
import random

p=-200
stop = 0
isFire = False
target = 0
harder = 0
def init():
    t.goto(-300,0)
    t.goto(300,0)
    global target, harder
    target = random.randint(50,150)
    harder = random.randint(0,10)

    t.pensize(3)
    t.color("green")
    t.up()
    t.goto(target - 25,2)
    t.down()
    t.goto(target + 25,2)

    t.pensize(3)
    t.color("orange")
    t.up()
    t.goto(harder - 15,2)
    t.down()
    t.goto(harder + 15,2)

    t.color("black")
    t.up()
    t.goto(-200,10)
    t.setheading(20)

    
def turn_up():
    t.left(2)
    
def turn_down():
    t.right(2)

def move_right():
    global p
    p+=1
    t.goto(p,10)

def move_left():
    global p
    p-=1
    t.goto(p,10)

def stop():
    global stop
    stop = 1


def fire():
    global isFire, stop, target, harder
    if not isFire:
        isFire = True
        stop = 0
        ang = t.heading()
        d = 0
        dis = 0
        while stop != 1:
            t.down()
            t.forward(random.randint(10,50))
            t.right(random.randint(5,100))
            d=t.distance(target,0)
            dis=t.distance(harder,0)
            t.up()
            if dis < 15 or d < 25:
                stop = 1
           
        t.sety(random.randint(10,100))
        if dis<15:
            t.color("orange")
            t.write("Great!!!", False, "center",("", 15))
        elif d<25:
            t.color("blue")
            t.write("Good!", False, "center",("",15))
        else:
            t.color("red")
            t.write("Bad!",False, "center",("",15))
            t.goto(-200,10)
            t.color("black")
            t.setheading(ang)
            isFire = False
            

init()
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire,"space")
t.onkeypress(move_right,"Right")
t.onkeypress(move_left, "Left")
t.onkeypress(stop, "Escape")
t.listen()

t.mainloop()
