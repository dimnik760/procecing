angle = 0
def setup():
    

    size(600,500)
    fill(139, 69, 19)
    frameRate(5)

def draw():
    global angle
    background(255)
    ellipse(320,65,20,20)
    ellipse(280,65,20,20)
    ellipse(300,110,80,80)
    ellipse(300,250,200,200)
    ellipse(340,345,50,50)
    ellipse(270,345,50,50)
    ellipse(310,100,15,15)
    ellipse(290,100,15,15)
    ellipse(300,115,15,15)
    rotate(radians(30))
    ellipse(290,90,40,80)
    translate(490,0)     
    rotate(radians(angle))
    ellipse(0,0,80,40)

    angle = angle + 90
