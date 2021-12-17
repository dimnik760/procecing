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
    fill(255, 69, 0)
    ellipse(120,0,50,90)
    ellipse(160,0,30,30)
    rotate(radians(130))
    fill(random(255),random(255),random(255))
    ellipse(60,0,90,50)
    fill(255, 69, 0)
    ellipse(120,0,50,90)
    fill(random(255),random(255),random(255))
    ellipse(160,0,30,30)
    rotate(radians(120))
    fill(random(255),random(255),random(255))
    ellipse(60,0,90,50)
    fill(255, 69, 0)
    ellipse(120,0,50,90)
    fill(random(255),random(255),random(255))
    ellipse(160,0,30,30)
    angle = angle + 1000000000000000000000
    x = x + 0.005
    if x >= 28-1:
        x = 0 
