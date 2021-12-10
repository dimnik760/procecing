x = 0
def setup():
    size(600,400)
def draw():
    global x
    background(255)
    #translate(300,200)
    rotate(radians(30))
    fill(random(255),random(255),random(255))
    ellipse(x,0,50,40) 
    x = x + 10
    if x >= 700-40:
        x = 0   
    
