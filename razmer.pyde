angle = 0
x = 0
def setup():
    size(600,400)
def draw():
    global angle
    global x
    background(100)
    translate(300,200)
    scale(x)
    fill(255,255,random(250))
    ellipse(0,0,30,30)
    rotate(radians(angle))
    ellipse(60,0,90,50)

    angle = angle + 1000000000000000000000
    x = x + 1
    if x >= 10-1:
        x = 0   
