angle = 100
def setup():
    size(600,400)
    point(300,200)
def draw():
    global angle
    translate(300,200)
    fill(random(255), random(255), random(255))
    stroke(random(255))
    rotate(radians(angle))    
    ellipse(20,50,90,50)
    angle = angle + 1
